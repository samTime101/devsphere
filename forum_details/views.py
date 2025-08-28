from django.shortcuts import render,redirect
from django.views import View
from sql_db.models import Forum , User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ForumDetailsView(LoginRequiredMixin, View):
    def get(self, request, forum_id):
        try:
            forum = Forum.objects.get(id=forum_id)
        except Forum.DoesNotExist:
            messages.error(request, "FORUM NOT FOUND!")
            return redirect('list_forums')

        return_response = {'forum': forum}
        return render(request, 'forum/detail.html', return_response)