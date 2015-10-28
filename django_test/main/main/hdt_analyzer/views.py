from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if settings.DEBUG:
        return render(request, 'index.html', {})
        #<!--{% url hdt_analyzer.views.process %}-->
if settings.DEBUG:
    @csrf_exempt
    def hi(request):
        files =  request.POST.get('files')
        print files[0].name