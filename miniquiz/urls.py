from django.urls import path
from miniquiz.views import *

app_name = 'miniquiz'

urlpatterns = [
    path('', show_quiz_homepage, name='show-quiz-homepage'),
    path('<pk>/', show_quiz_mainpage, name='show-quiz-mainpage'),
    path('<pk>/data/', show_quiz_json, name='show-quiz-json'),
    path('<pk>/save', save_quiz, name='save-quiz'),
]