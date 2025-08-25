# SAMIP REGMI
# AUGUST 25

from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('index')
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        messages.success(request, 'Account created successfully')
        return render(request, 'signup.html')
