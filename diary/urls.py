from django.urls import path
from diary.views import *

app_name = 'diary'

urlpatterns = [
    path('create_log/', create_log, name='create_log'),
    path('', show_diary, name='show_diary'),
    path('get_json/', get_diarylog_json, name='get_json'),
    path('delete_log/<int:pk>/', delete_log, name='delete_log'),
    path('update_log/<int:id>', update_log, name='update_log'),


]