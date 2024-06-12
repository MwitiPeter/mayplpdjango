# from django.shortcuts import render
from django.http import HTTPResponse

# Create your views here.
 def index(request):
   return HttpResponse("My first webpage with python Django")