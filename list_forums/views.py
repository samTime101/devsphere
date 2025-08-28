from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.views import View
from sql_db.models import Forum , User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ListForumsView(LoginRequiredMixin, View):
    def get(self, request):
        forums = Forum.objects.all().order_by('-created_at')
        return_response = {'forums': forums}
        return render(request, 'forum/list.html', return_response)