#from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def home(request, id):
    if request.method == 'POST':
        context = {
            'name': request.POST['name']
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')
