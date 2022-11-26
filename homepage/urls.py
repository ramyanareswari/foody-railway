from django.urls import path
from homepage.views import show_homepage
from homepage.views import register
from homepage.views import login_user
from homepage.views import logout_user
# ========= flutter =========
from homepage.views import login_flutter
from homepage.views import register_flutter
from homepage.views import logout_flutter
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('loginflutter', login_flutter, name='login_flutter'),
    path('registerflutter',register_flutter,name='register_flutter'),
    path('logoutflutter',logout_flutter,name='logout_flutter'),
]