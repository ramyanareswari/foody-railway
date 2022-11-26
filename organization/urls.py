from django.urls import path
from .views import *

app_name = 'organization'

urlpatterns = [
    path('', show_organization, name='show_organization'),
    path('organization/', add_organization, name='add_organization'),
    path('json/', json, name='json'),
]