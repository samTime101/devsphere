from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Event, EventImage

class EventRegisterView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request): 
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        print(Event.STATUS_CHOICES)
        return_context = {
            'status_choices': Event.STATUS_CHOICES
        }
        return render(request, 'admin/event/create.html', context=return_context)

    def post(self, request):
        event_data = {
            'name': request.POST.get('name'),
            'date': request.POST.get('date'),
            'location': request.POST.get('location'),
            'description': request.POST.get('description'),
            'event_starting_date_time': request.POST.get('event_starting_date_time'),
            'event_ending_date_time': request.POST.get('event_ending_date_time'),
            'organized_by': request.POST.get('organized_by', 'BIC Devsphere'),
            'event_guest_speaker': request.POST.get('event_guest_speaker', ''),
            'event_guest_speaker_bio': request.POST.get('event_guest_speaker_bio', ''),
            'registration_link': request.POST.get('registration_link', ''),
            'status': request.POST.get('status', 'upcoming'),
        }

        banner_image = request.FILES.get('banner_image')
        guest_speaker_image = request.FILES.get('event_guest_speaker_image')
        event_images = request.FILES.getlist('event_images')

        required_fields = [
            event_data['name'], event_data['date'], event_data['location'],
            event_data['description'], event_data['event_starting_date_time'],
            event_data['event_ending_date_time'], event_data['status'],
            banner_image, guest_speaker_image
        ]
        if not all(required_fields):
            messages.error(request, 'PLEASE FILL IN ALL REQUIRED FIELDS.')
            return redirect('create_event')

        event = Event.objects.create(**event_data)

        if banner_image:
            event.banner_image = banner_image
        if guest_speaker_image:
            event.event_guest_speaker_image = guest_speaker_image
        event.save()  

        for idx, image in enumerate(event_images, start=1):
            ext = image.name.split('.')[-1]
            image.name = f"event_{event.id}_image_{idx}.{ext}"
            EventImage.objects.create(event=event, image=image)

        messages.success(request, "EVENT CREATED SUCCESSFULLY")
        return redirect('admin')


