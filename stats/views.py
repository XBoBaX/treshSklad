from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from Profile.models import Profile
from datetime import datetime, timedelta
from WarehouseSpace.models import WarehouseSpace
from traffic.models import Traffic
from unload.models import Unloader
from django.http import JsonResponse

def getSt(request):
    form = request.GET
    date = form["date"]
    sk = form["sk"]
    if date == "0":
        dateL = datetime.now()
    else:
        year1 = int(datetime.now().year)
        mounth1 = int(date)
        dateL = datetime(year1, mounth1, 1)
    if sk == "9999999":
        trafficNow = Traffic.objects.filter(status="Принят", dateUpload__month=dateL.month)
        trafficWait = Traffic.objects.filter(status="Отправлен", dateArrival__month=dateL.month)
    else:
        trafficNow = Traffic.objects.filter(status="Принят", dateUpload__month=dateL.month, sklad=WarehouseSpace.objects.get(id=sk))
        trafficWait = Traffic.objects.filter(status="Отправлен", dateArrival__month=dateL.month, sklad=WarehouseSpace.objects.get(id=sk))

    unload_now = Unloader.objects.filter(status="Отправлен", dateUpload__month=dateL.month)
    trW1 = 0
    trW2 = 0
    trW3 = 0
    trW4 = 0
    for ch in trafficWait:
        if ch.dateArrival.weekday() == 1:
            trW1 += 1
        elif ch.dateArrival.weekday() == 2:
            trW2 += 1
        elif ch.dateArrival.weekday() == 3:
            trW3 += 1
        elif ch.dateArrival.weekday() == 4:
            trW4 += 1
    trN1 = 0
    trN2 = 0
    trN3 = 0
    trN4 = 0
    for ch in trafficNow:
        if ch.dateArrival.weekday() == 1:
            trN1 += 1
        elif ch.dateArrival.weekday() == 2:
            trN2 += 1
        elif ch.dateArrival.weekday() == 3:
            trN3 += 1
        elif ch.dateArrival.weekday() == 4:
            trN4 += 1
    unN1 = 0
    unN2 = 0
    unN3 = 0
    unN4 = 0
    for ch in unload_now:
        if ch.dateArrival.weekday() == 1:
            unN1 += 1
        elif ch.dateArrival.weekday() == 2:
            unN2 += 1
        elif ch.dateArrival.weekday() == 3:
            unN3 += 1
        elif ch.dateArrival.weekday() == 4:
            unN4 += 1
    data = {"trN1": trN1, "trN2": trN2, "trN3": trN3, "trN4": trN4,
            "trW1": trW1, "trW2": trW2, "trW3": trW3, "trW4": trW4,
            "unN1": unN1, "unN2": unN2, "unN3": unN3, "unN4": unN4}
    return JsonResponse(data)


def show_index(request):
    sklad = WarehouseSpace.objects.all()

    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        us_name = us_name[:10]
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    data = {"index": 9, "us_name": us_name, "type_user": type_user, "sk": sklad}
    return render(request, "index1.html", context=data)
