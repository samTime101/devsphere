# SAMiP REGMI
# AUGUST 25

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages

class SigninView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'YOU ARE ALREADY LOGGED IN')
            return redirect('index')
        return render(request, 'signin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'INVALID USERNAME OR PASSWORD')
            return render(request, 'signin.html')
