"""from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def addContent(request):
    if request.method == 'POST':
        image1 = request.POST['image1']
        image2 = request.POST['image2']
        place1 = request.POST['place1']
        place2 = request.POST['place2']
        date = request.POST['date']
        personname = request.POST['personname']
        aboutperson = request.POST['aboutperson']
        aboutplace = request.POST['aboutplace']

        user = Destinations(image1 = image1,image2 = image2, place1 = place1,place2 = place2,date = date, personname = personname,aboutperson = aboutperson, aboutplace = aboutplace)
        user.save()
        print("User Created")
        messages.info(request,"Succefully uploaded")
        return redirect('blog.html')

    else:
        return render(request,"addContent.html")"""
