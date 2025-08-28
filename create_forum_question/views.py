from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Forum, Question

class CreateForumQuestionView(LoginRequiredMixin, View):
    def post(self, request, forum_id):
        question_content = request.POST.get('content', '').strip()
        question_title = request.POST.get('title', '').strip()

        if not question_title or not question_content:
            messages.error(request, "TITLE AND CONTENT CANNOT BE EMPTY!")
            return redirect('forum_detail', forum_id=forum_id)

        forum = get_object_or_404(Forum, id=forum_id)
        Question.objects.create(
            forum=forum,
            title=question_title,
            content=question_content,
            created_by=request.user
        )
        messages.success(request, "QUESTION CREATED SUCCESSFULLY!")
        return redirect('forum_detail', forum_id=forum_id)
