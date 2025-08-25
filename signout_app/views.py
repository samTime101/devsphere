# AUGUST 25
# SAMIP REGMI

from django.contrib.auth import logout
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class SignoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        messages.success(request, 'YOU HAVE BEEN LOGGED OUT')
        return redirect('signin')
