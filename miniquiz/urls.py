from django.urls import path
from miniquiz.views import *

app_name = 'miniquiz'

urlpatterns = [
    path('', show_quiz_homepage, name='show-quiz-homepage'),
    
    path('get-quiz-model/', get_quiz_model, name='get-quiz-model'),
    path('get-quiz-beneran/<pk>', get_quiz_beneran, name='get-quiz-beneran'),
    path('get-quiz-model/<pk>', get_question, name='get-question'),
    path('get-quiz-model/<pk>/<pk2>', get_option, name='get-option'),
    path('get-quiz-model/<pk>/save', save_assessment, name='save-assessment'),

    path('<int:pk>/', show_quiz_mainpage, name='show-quiz-mainpage'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<pk>/save', save_quiz, name='save-quiz'),
]