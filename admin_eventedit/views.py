from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Event, EventImage

class EventEditView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request, event_id): 
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            messages.error(request, 'Event not found.')
            return redirect('admin')
        return_context = {
            'event': event,
            'status_choices': Event.STATUS_CHOICES
        }
        return render(request, 'admin/event/edit.html', context=return_context)

    def post(self, request, event_id):
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            messages.error(request, 'Event not found.')
            return redirect('admin')
        event.name = request.POST.get('name')
        event.date = request.POST.get('date')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        event.event_starting_date_time = request.POST.get('event_starting_date_time')
        event.event_ending_date_time = request.POST.get('event_ending_date_time')
        event.organized_by = request.POST.get('organized_by', 'BIC Devsphere')
        event.event_guest_speaker = request.POST.get('event_guest_speaker', '')
        event.event_guest_speaker_bio = request.POST.get('event_guest_speaker_bio', '')
        event.registration_link = request.POST.get('registration_link', '')
        event.status = request.POST.get('status', 'Upcoming')   


        if request.FILES.get('banner_image'):
            event.banner_image = request.FILES['banner_image']
        if request.FILES.get('event_guest_speaker_image'):
            event.event_guest_speaker_image = request.FILES['event_guest_speaker_image']
        event.save()

        for image in request.FILES.getlist('event_images'):
            EventImage.objects.create(event=event, image=image)

        messages.success(request, "EVENT UPDATED SUCCESSFULLY")
        return redirect('admin')
