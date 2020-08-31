from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    d=Destination.objects.all()
    return render(request , 'index.htm' , {'d':d})