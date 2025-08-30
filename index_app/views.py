# SAMIP REGMI
# AUGUST 25

# SAMIP REGMI
# AUGUST 27
# SENDING USER DETAILS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from sql_db.models import Event, User


class IndexView(LoginRequiredMixin, View):
    login_url = "/signin/"

    def get(self, request):
        # MESSAGE LOGIN VAYE PAXI EK CHOTI MATRA DEKHAUNE & THEN WE POP IT OUT
        if request.session.pop('loggined_in', False):
            messages.success(request, "WELCOME TO HOME PAGE")
        events = Event.objects.all().order_by("-date")  # [:3]
        user = User.objects.get(username=request.user.username)
        return_context = {"events": events, "user": user}
        return render(request, "index.html", context=return_context)
