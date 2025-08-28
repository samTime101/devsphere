# AUGUST 28
# SAMIP REGMI

from django.shortcuts import render
from django.views import View
from sql_db.models import Blogs 
from django.contrib.auth.mixins import LoginRequiredMixin

class ListBlogsView(LoginRequiredMixin, View):
    login_url = '/signin/'  

    def get(self, request):
        blogs = Blogs.objects.all().order_by('-created_at')
        return_response = {
            'blogs': blogs
        }
        return render(request, 'blog/list.html', return_response)