
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
def show_organization(request):
    info=Information.objects.all()
    context={
        'organization':info
    }
    return render(request,"organization.html",context)

def json(request):
    data=Information.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 
    
def add_organization(request):
    if request.method == 'POST' :
        title = request.POST.get('title')
        description = request.POST.get('description')
        Information.objects.create(title = title,description = description )
        return JsonResponse({'title' : title,'description' : description}, status=200)
    
