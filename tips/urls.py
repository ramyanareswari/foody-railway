from audioop import add
from django.urls import path
from tips.views import *

app_name = 'tips'

urlpatterns = [
    path('', show_tips_article, name='show_tips_article'),
    path('add-article/', add_article, name='add_article'),
    path('json/', get_article, name='get_article'),
    path('<id>/', detail_article, name='detail_article'),
]