from django.shortcuts import render
from mysite import models

# Create your views here.

def index(request):
    return render(request, "index.html")