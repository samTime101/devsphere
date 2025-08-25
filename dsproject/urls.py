# SAMIP REGMI 
# AUGUST 25 

from django.contrib import admin
from django.urls import path

from signout_app.views import SignoutView
from signup_app.views import SignupView
from signin_app.views import SigninView
from index_app.views import IndexView
from admin_app.views import AdminView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', AdminView.as_view(), name='admin'),
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignoutView.as_view(), name='signout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)