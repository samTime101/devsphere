from django.shortcuts import render
from django.views import View
from sql_db.models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class UserBlogsView(LoginRequiredMixin, View):
    login_url = '/signin/'  

    def get(self, request):
        user_blogs = Blogs.objects.filter(author=request.user).order_by('-created_at')
        return_response = {
            'user_blogs': user_blogs
        }
        return render(request, 'blog/user.html', return_response)