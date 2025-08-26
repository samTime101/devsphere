# SAMIP REGMI 
# AUGUST 26

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import DiscordMember

class MembersListView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        members = DiscordMember.objects.all().order_by('name')
        return render(request, 'members.html', {'members': members})
