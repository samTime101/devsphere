from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Answer, Vote

class VoteAnswerView(LoginRequiredMixin, View):
    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)
        user = request.user
        value = request.POST.get('value')

        if value not in ['1', '-1']:
            return redirect('forum_question_detail', question_id=answer.question.id)

        value = int(value)

        try:
            vote = Vote.objects.get(user=user, answer=answer)
            if vote.value == value:
                vote.delete() 
            else:
                vote.value = value
                vote.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, answer=answer, value=value)

        return redirect('forum_question_detail', question_id=answer.question.id)
