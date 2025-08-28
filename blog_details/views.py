from django.shortcuts import redirect, render
from django.views import View
from sql_db.models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class BlogDetailView(LoginRequiredMixin, View):
    login_url = '/signin/'  

    def get(self, request, blog_id):
        try:
            blog = Blogs.objects.get(id=blog_id, approved=True)
        except Blogs.DoesNotExist:
            messages.error(request, "BLOG NOT FOUND OR NOT APPROVED")
            return redirect('/blogs/')
        return_context = {
            'blog': blog
        }
        return render(request, 'blog/detail.html', return_context)
