from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request, 'sale/home.html', context)
 
def about(request):
    return render(request, 'sale/about.html', {'title':'About'})