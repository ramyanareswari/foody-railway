from django.urls import path
from expiry.views import *

app_name = 'expiry'

urlpatterns = [
    path('', show_expiry, name='show_expiry'),
    path('add-food/', add_food, name='add_food'),
    path('add-food-flutter', add_food_flutter, name='add_food_flutter'),
    path('delete-food/<str:id>', delete_food, name='delete_food'),
    path('json/', show_json, name='show_json'),
]