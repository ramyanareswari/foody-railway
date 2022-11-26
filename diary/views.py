from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='/login/')
def show_diary(request):
    res = 0
    for data in Diary.objects.filter(user=request.user):
       res += data.price
    context = {
        'user': request.user,
        'res' : res
    }
    return render(request, 'diary.html', context)

@csrf_exempt
@login_required(login_url='/login/')
def create_log(request):
    val = True
    if request.method == 'POST':
        foodname = request.POST.get('foodname')
        description = request.POST.get('description')
        date = request.POST.get('date')
        price = request.POST.get('price')

        # if habis = checked return true, if tidak habis return false
        log = Diary.objects.create(
            user=request.user,
            foodname=foodname,
            description=description,
            date=date,
            is_finished = False,
            price=price)
            
        return JsonResponse(
            {
                'pk': log.id,
                'fields': {
                    'title': log.foodname,
                    'description': log.description,
                    'date': log.date,
                    'is_finished': log.is_finished,
                    'price': log.price
                },
            },
            status=200,
        )

@login_required(login_url='/login/')
def get_diarylog_json(request):
    data = Diary.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def delete_log(request, pk):
    if Diary.objects.get(pk = pk).user == request.user:
        Diary.objects.filter(pk = pk).delete()
    return redirect('diary:show_diary')

@login_required(login_url='/login/')
def update_log(request, id):
    log = Diary.objects.get(user=request.user, id=id)
    log.is_finished = not log.is_finished
    log.save()
    return redirect('diary:show_diary')