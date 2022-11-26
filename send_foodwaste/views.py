from django.shortcuts import render, redirect
from send_foodwaste.models import Send_FoodWaste_Model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from send_foodwaste.forms import FoodwasteForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def show_foodwaste(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'send_foodwaste.html', context)

@login_required(login_url='/login/')
def show_foodwaste_json(request):
    data = Send_FoodWaste_Model.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  

@login_required(login_url='/login/')
def add_foodwaste(request):
    if request.method == "POST":
        # user = request.user
        # name = request.POST.get('name')
        # phone_number = request.POST.get('phone_number')
        # address = request.POST.get('address')
        # food_type = request.POST.get('food_type')
        # expiry_date = request.POST.get('expiry_date')
        # weight = request.POST.get('weight')

        # new_foodwaste = Send_FoodWaste_Model(user = user, name = name, phone_number = phone_number, address = address, food_type = food_type, expiry_date = expiry_date, weight = weight)
        # new_foodwaste.save()
        # return JsonResponse({
        #     'name' : name,
        #     'phone_number' : phone_number,
        #     'address' : address,
        #     'food_type' : food_type,
        #     'expiry_date' : expiry_date,
        #     'weight' : weight
        # })
        form = FoodwasteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form_save = form.save()
            return JsonResponse({
                'data' : form.data,
                'id': form_save.id
            })
        
@login_required(login_url='/login/')
def delete_foodwaste(request, pk):
    if Send_FoodWaste_Model.objects.get(pk = pk).user == request.user:
        Send_FoodWaste_Model.objects.filter(pk = pk).delete()
    return redirect('send_foodwaste:show_foodwaste')