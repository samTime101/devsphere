from django.shortcuts import get_object_or_404, redirect, render 
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Forum, Question, Vote


class ForumQuestionDetailView(LoginRequiredMixin, View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        forum = question.forum
        answers = question.answers.all()
        if not forum:
            messages.error(request, "FORUM NOT FOUND!")
            return redirect('list_forums')
        context = {
            'question': question,
            'forum': forum,
            'answers': answers,
        }
        return render(request, 'forum/question/detail.html', context)
    
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        if request.method == "POST":
            content = request.POST.get("content")
            if content:
                question.answers.create(content=content, created_by=request.user)
                messages.success(request, "YOUR ANSWER HAS BEEN POSTED!")
            else:
                messages.error(request, "PLEASE PROVIDE AN ANSWER.")
        return redirect('forum_question_detail', question_id=question.id)