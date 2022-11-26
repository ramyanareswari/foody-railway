
from contextlib import redirect_stderr
from django.shortcuts import redirect, render
from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from tips.forms import AddArticle

from django.views.decorators.csrf import csrf_exempt


from tips.models import TipsArticle

# =============== Show all article =============== #
def show_tips_article(request):
    if request.user.is_authenticated:
        articles = TipsArticle.objects.all()

        context = {
            'author': request.user.username,
            'articles': articles,
            'form': AddArticle()
        }
        return render(request, 'tips.html', context)    
    else:
        return render(request, "tips_public.html")
    

# =============== Add article modal =============== #
@login_required(login_url='/login/')
@csrf_exempt
def add_article(request):

    form = AddArticle(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        art = form.save(commit=False)
        art.author = User.objects.get(username = request.user)
        art.save()
        
        response = {
                'pk': art.id,
                'author': art.author.username,
                'title': art.title,
                'content': art.content,
                'publish': art.publish,
                'url' : '/tips/'
                }
        return HttpResponse(response)
    return render(request, "tips.html", {'form': AddArticle()})
        

#  ==== view AJAX which returns a JSON object from json database ====
def get_article(request):
    tipsObj = TipsArticle.objects.filter(author = request.user)

    data = serializers.serialize('json', tipsObj)
    return HttpResponse(data, content_type="application/json")

# =============== Detail article =============== #
@login_required(login_url='/login/')
def detail_article(request, id):
    articles = TipsArticle.objects.get(pk=id)

    context = {
        'articles': articles,
    }

    return render(request, 'detail.html', context)


