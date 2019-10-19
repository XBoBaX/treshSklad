from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from Profile.models import Profile
from .models import Transport
from datetime import datetime


def add_car(request):
    form = request.GET
    name1 = form["name"]
    normal_Den = form["normal_Den"]
    normal = form["normal"]
    type = form["type"]
    truck = form["truck"]
    if truck == "Перевозка":
        truck = True
    else:
        truck = False
    count = form["count"]
    car = Transport.objects.create(name=name1, HoursDay=normal_Den, allHours=normal,
                                   bTrucker=truck, coutPallet=count, typeTransport=type,
                                   dateEditStatus=datetime.now())
    return HttpResponse('', content_type='text/html')


def show_index(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        us_name = us_name[:10]
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    car = Transport.objects.all()
    data = {"index": 6, "us_name": us_name, "type_user": type_user, "car": car}
    return render(request, "index1.html", context=data)

