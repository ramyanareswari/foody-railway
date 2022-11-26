from django.urls import path
from homepage.views import show_homepage
from homepage.views import register
from homepage.views import login_user
from homepage.views import logout_user
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]