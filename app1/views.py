from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('This is first application of app1')
def app1_second(request):
    return HttpResponse('<h1><marquee>This is second application of app1</h1></marquee>')