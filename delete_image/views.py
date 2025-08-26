# AUGUST 26
# SAMIP REGMI
from pyexpat.errors import messages
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import EventImage , Event
class DeleteImageView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def post(self, request):
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')

        image_id = request.POST.get('image_id')
        banner = request.POST.get('banner') 
        speaker = request.POST.get('speaker') 

        if image_id:  
            try:
                image = EventImage.objects.get(id=image_id)
                event_id = image.event.id
                image.delete()
                return redirect('edit_event', event_id=event_id)
            except EventImage.DoesNotExist:
                return redirect('admin')

        elif banner or speaker: 
            event_id = request.POST.get('event_id')
            event = Event.objects.get(id=event_id)
            if banner:
                event.banner_image.delete(save=True)
            if speaker:
                event.event_guest_speaker_image.delete(save=True)
            return redirect('edit_event', event_id=event_id)

        return redirect('admin')
