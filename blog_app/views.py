# AUGUST 28
# SAMIP REGMI
from django.shortcuts import render, redirect
from django.views import View
from sql_db.models import Blogs , User
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateBlogView(LoginRequiredMixin, View):
    login_url = '/signin/'  

    def get(self, request):
        return render(request, 'blog/create.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        new_blog = Blogs(title=title, content=content, author=author)
        new_blog.save()

        return_response = {
            'message': 'BLOG CREATED SUCCESSFULLY',
            'blog': {
                'title': new_blog.title,
                'author': new_blog.author.username,
                'created_at': new_blog.created_at
            }
        }
        return redirect('/myblogs/') 
