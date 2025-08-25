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
            'status': request.POST.get('status', 'Upcoming'),
        }
        event_data['banner_image'] = request.FILES.get('banner_image')
        event_data['event_guest_speaker_image'] = request.FILES.get('event_guest_speaker_image')

        if not all([event_data['name'], event_data['date'], event_data['location'],
                    event_data['description'], event_data['event_starting_date_time'],
                    event_data['event_ending_date_time'],event_data['status'],
                    event_data['banner_image'], event_data['event_guest_speaker_image'],
                    event_data['event_guest_speaker_bio'],
                    event_data['registration_link']
                    ]):
            
            messages.error(request, 'PLEASE FILL IN ALL REQUIRED FIELDS.')
            return redirect('create_event')

        if request.FILES.get('banner_image'):
            event_data['banner_image'] = request.FILES['banner_image']
        if request.FILES.get('event_guest_speaker_image'):
            event_data['event_guest_speaker_image'] = request.FILES['event_guest_speaker_image']

        event = Event.objects.create(**event_data)

        for image in request.FILES.getlist('event_images'):
            EventImage.objects.create(event=event, image=image)

        messages.success(request, "EVENT CREATED SUCCESSFULLY")
        return redirect('admin')
