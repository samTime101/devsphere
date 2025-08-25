from django.shortcuts import render
from django.views import View
from sql_db.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin

class EventListView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request,event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            event = None
        return_context = {
            'event': event,
        }

        return render(request, 'event/detail.html', context=return_context)