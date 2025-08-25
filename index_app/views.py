# SAMIP REGMI
# AUGUST 25

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.contrib import messages

class IndexView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        messages.info(request, 'WELCOME TO HOME PAGE')
        return render(request, 'index.html')
