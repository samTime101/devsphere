# SAMIP REGMI
# AUGUST 28

from django.shortcuts import redirect, render
from django.views import View
from sql_db.models import Blogs , User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class BlogApprovalView(LoginRequiredMixin, View):
    login_url = '/signin/'  

    def get(self, request):
        if not request.user.is_superuser:
            messages.error(request, "UNAUTHORIZED ACCESS")
            return render(request,"index.html")

        blogs = Blogs.objects.order_by('-created_at')
        return_context = {'blogs': blogs}
        return render(request, 'admin/blog/list.html', return_context)

    def post(self, request):
        if not request.user.is_superuser:
            messages.error(request, "UNAUTHORIZED ACCESS")
            return render(request, 'index.html')


        blog_id = request.POST.get('blog_id')
        action = request.POST.get('action')

        try:
            blog = Blogs.objects.get(id=blog_id)
            if action == 'approve':
                blog.approved = True
                blog.save()
            elif action == 'reject':
                blog.delete()
        except Blogs.DoesNotExist:
            messages.error(request, "BLOG NOT FOUND")
            return render(request, 'index.html')

        messages.success(request, "ACTION COMPLETED SUCCESSFULLY")
        return redirect('/admin/blogs/approval/')