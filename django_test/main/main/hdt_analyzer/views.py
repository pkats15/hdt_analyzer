from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    if settings.DEBUG:
        return render(request, 'index.html', {})