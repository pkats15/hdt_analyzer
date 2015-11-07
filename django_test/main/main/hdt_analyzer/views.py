from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
import core.online_file_manager as ofm
import json
import startup
import traceback


# Create your views here.

# TODO Add zip support

def index(request):
    if settings.DEBUG:
        return render(request, 'index.html', {})
        # <!--{% url hdt_analyzer.views.process %}-->


if settings.DEBUG:
    @csrf_exempt
    def hi(request):
        print 'hi'
        if settings.DEBUG or request.is_ajax():
            print 'hi2'
            if len(request.FILES) == 1:
                files = request.FILES
                file_list = []
                for k, v in files.items():
                    file_list.append(v)
                c = startup.ofm.add_file(file_list[0])
                try:
                    startup.ofm.unzip_to_tmp(startup.ofm.get_file(c))
                except:
                    traceback.print_exc()
                response = JsonResponse({'code': c})
                return response
