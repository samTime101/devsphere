# SAMIP REGMI
# AUGUST 25

# AUGUST 27
# ADDED STREAM AND SECTION FIELDS

from django.views import View
from django.shortcuts import redirect, render
from sql_db.models import User
from django.contrib import messages

class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'YOU ARE ALREADY LOGGED IN.')
            return redirect('index')
        return_context = {
            'streams': User.STREAM_CHOICES,
            'sections': User.SECTION_CHOICES,
        }
        return render(request, 'signup.html', context=return_context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        stream = request.POST.get('stream')
        section = request.POST.get('section')

        # CHECK IF USER ALREADY EXISTS
        if User.objects.filter(username=username).exists():
            messages.error(request, 'USERNAME ALREADY EXISTS')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password, email=email, stream=stream, section=section)
        user.save()

        messages.success(request, 'ACCOUNT CREATED SUCCESSFULLY')
        return render(request, 'signup.html')
