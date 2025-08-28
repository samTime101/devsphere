# SAMIP REGMI
# AUGUST 25

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from signout_app.views import SignoutView
from signup_app.views import SignupView
from signin_app.views import SigninView
from index_app.views import IndexView
from admin_app.views import AdminView
from admin_eventdelete.views import EventDeleteView
from admin_eventregister.views import EventRegisterView
from admin_eventedit.views import EventEditView
from event_app.views import EventListView
from delete_image.views import DeleteImageView
from members_list.views import MembersListView
from blog_app.views import CreateBlogView
from list_blogs.views import ListBlogsView
from admin_blogapproval.views import BlogApprovalView
from blog_details.views import BlogDetailView
from user_blogs.views import UserBlogsView
from create_forum.views import CreateForumView
from list_forums.views import ListForumsView
from forum_details.views import ForumDetailView
from create_forum_question.views import CreateForumQuestionView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', AdminView.as_view(), name='admin'),
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('create/event/', EventRegisterView.as_view(), name='create_event'),
    path('edit/event/<int:event_id>/', EventEditView.as_view(), name='edit_event'),
    path('event/<int:event_id>/', EventListView.as_view(), name='event_detail'),
    path('delete/event/<int:event_id>/', EventDeleteView.as_view(), name='delete_event'),
    path('delete/image/', DeleteImageView.as_view(), name='delete_image'),
    path('members/', MembersListView.as_view(), name='members_list'),
    path('create/blog/', CreateBlogView.as_view(), name='create_blog'),
    path('blogs/', ListBlogsView.as_view(), name='list_blogs'),
    path('admin/blogs/approval/', BlogApprovalView.as_view(), name='blog_approval'),
    path('blog/<int:blog_id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('myblogs/', UserBlogsView.as_view(), name='user_blogs'),
    path('create/forum/', CreateForumView.as_view(), name='create_forum'),
    path('forums/', ListForumsView.as_view(), name='list_forums'),
    path('forum/<int:forum_id>/', ForumDetailView.as_view(), name='forum_detail'),
    path('forum/<int:forum_id>/ask/', CreateForumQuestionView.as_view(), name='create_forum_question'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
