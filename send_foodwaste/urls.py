from django.urls import path
from send_foodwaste.views import *

app_name = 'send_foodwaste'

urlpatterns = [
    path('', show_foodwaste, name='show_foodwaste'),
    path('add_foodwaste/', add_foodwaste, name='add_foodwaste'),
    path('delete_foodwaste/<int:pk>/', delete_foodwaste, name='delete_foodwaste'),
    path('json/', show_foodwaste_json, name='show_foodwaste_json')
]