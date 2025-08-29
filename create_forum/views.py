# SAMIP REGMI
# AUGUST 28

from django.shortcuts import render, redirect
from django.views import View
from sql_db.models import Forum , User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateForumView(LoginRequiredMixin, View):
    login_url = '/signin/'
    def get(self, request):
        return render(request, 'forum/create.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_by = request.user

        if not title or not description:
            messages.error(request, "TITLE AND DESCRIPTION ARE REQUIRED!")
            return redirect('create_forum')

        forum = Forum.objects.create(
            name=title,
            description=description,
            created_by=created_by
        )
        forum.save()
        messages.success(request, "FORUM CREATED SUCCESSFULLY!")
        return redirect('forum_detail', forum_id=forum.id)