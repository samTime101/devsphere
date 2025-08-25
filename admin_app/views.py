# SAMIP REGMI
# AUGUST 25

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from sql_db.models import Event     
class AdminView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        messages.info(request, 'WELCOME TO ADMIN DASHBOARD')
        events = Event.objects.all()
        return_context = {
            'events': events,
        }
        return render(request, 'admin/admin.html', context=return_context)