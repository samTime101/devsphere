# SAMIP REGMI 
# AUGUST 25 

from django.contrib import admin
from django.urls import path

from signout_app.views import SignoutView
from signup_app.views import SignupView
from signin_app.views import SigninView
from index_app.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignoutView.as_view(), name='signout'),
]
