from django.shortcuts import render , redirect
from django.views import View
from sql_db.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class EventDeleteView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request, event_id):
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            messages.success(request, "EVENT DELETED SUCCESSFULLY")
        except Event.DoesNotExist:
            messages.error(request, 'Event not found.')
        return redirect('admin')