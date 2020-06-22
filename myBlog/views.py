from django.shortcuts import render
from .models import Destinations
# Create your views here.
def home(request):
    dests = Destinations.objects.all()
    return render(request,"blog.html",{'dests':dests})
