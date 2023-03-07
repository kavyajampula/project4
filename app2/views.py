from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('This is application1 of app2')
def app2_second(request):
    return HttpResponse('This is application2 of app2')

