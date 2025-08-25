# SAMIP REGMI
# AUGUST 25

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from sql_db.models import Event, EventImage


class IndexView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        messages.info(request, 'WELCOME TO HOME PAGE')
        events = Event.objects.all().order_by('-date')[:3]
        context = {
            "events": events,

        }
        return render(request, 'index.html', context=context)
