from expiry.models import Food_Data
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
def show_expiry(request):
    # food_data = Food_Data.objects.filter(user = request.user).order_by('-food_expired_date')
    if request.user.is_authenticated:
        context = {
            # 'query_set_food': food_data,
            'today': datetime.date.today(),
            'username': request.user,
        }
        return render(request, "expiry.html", context)
    else:
        return render(request, "expiry_public.html")

@csrf_exempt
def add_food(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            food_name = request.POST.get('food_name')
            food_expired_date = request.POST.get('food_expired_date')
            food = Food_Data.objects.create(user = request.user, food_name = food_name, food_expired_date = food_expired_date)
            return JsonResponse(
                {
                    'pk': food.pk,
                    'fields': {
                        'food_name': food.food_name,
                        'food_expired_date': food.food_expired_date
                    },
                },
                status=200,
            )
    else:
        return render(request, "expiry_public.html")

def delete_food(request, id):
    if request.user.is_authenticated:
        foods = Food_Data.objects.get(user = request.user, id = id)
        foods.delete()
        return redirect('expiry:show_expiry')
    else:
        return render(request, "expiry_public.html")

def show_json(request):
    if request.user.is_authenticated:
        foods = Food_Data.objects.filter(user = request.user).order_by('food_expired_date')
        return HttpResponse(serializers.serialize("json", foods), content_type="application/json")
    else:
        return render(request, "expiry_public.html")