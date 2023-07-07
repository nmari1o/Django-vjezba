from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    # Add your view logic here
    return HttpResponse("This is my view!")
