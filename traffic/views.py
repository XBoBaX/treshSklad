from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib import auth
from Profile.models import Profile
from .models import Traffic
from products.models import Product
from transport.models import Transport
from unload.models import Unloader
from WarehouseSpace.models import WarehouseSpace
import time


def stopTraffic2(request, id1, id3):
    unl = Unloader.objects.get(id=id1)
    status = id3
    try:
        car = Transport.objects.filter(unloadsTr=unl, status="Используется")[0]
        car.status = "Простой"
        d1 = datetime.now()
        d2 = car.dateEditStatus
        d2 = d2.replace(tzinfo=None)
        min = (d1 - d2).total_seconds() / 60
        min = int(min)
        car.timeUse += min
        car.save()
    except Exception:
        print()

    if status == "cancell":
        unl.status = "Отменен"
    else:
        unl.status = "Принят"
    unl.unloads = False
    pr = Product.objects.filter(Unloader=unl)
    for ch in pr:
        ch.status = unl.status
        ch.dateUpload = datetime.now()
        ch.save()
    d1 = datetime.now()
    d2 = unl.dateUpload
    d2 = d2.replace(tzinfo=None)
    min = (d1 - d2).total_seconds() / 60
    min = int(min)
    unl.timeProc += min

    unl.save()
    return HttpResponse('', content_type='text/html')


def stopTraffic3(request, id1):
    trf = Unloader.objects.get(id=id1)
    try:
        cars = Transport.objects.filter(unloadsTr=trf, status="Используется")
        for car in cars:
            car.status = "Простой"
            d1 = datetime.now()
            d2 = car.dateEditStatus
            d2 = d2.replace(tzinfo=None)
            min = (d1 - d2).total_seconds()/60
            min = int(min)
            car.timeUse += min
            car.save()
    except Exception:
        print()

    trf.status = "Отправлен"
    trf.loads = False

    pr = Product.objects.filter(Unloader=trf)
    for ch in pr:
        ch.status = trf.status
        ch.dateUpload = datetime.now()
        ch.save()
    d1 = datetime.now()
    d2 = trf.dateUpload
    d2 = d2.replace(tzinfo=None)
    min = (d1 - d2).total_seconds() / 60
    min = int(min)
    trf.timeProc += min

    trf.save()
    return HttpResponse('', content_type='text/html')


def stopTraffic(request, id1, id3):
    trf = Traffic.objects.get(id=id1)
    status = id3
    try:
        car = Transport.objects.filter(unloads=trf, status="Используется")[0]
        car.status = "Простой"
        d1 = datetime.now()
        d2 = car.dateEditStatus
        d2 = d2.replace(tzinfo=None)
        min = (d1 - d2).total_seconds()/60
        min = int(min)
        car.timeUse += min
        car.save()
    except Exception:
        print()

    if status == "cancell":
        trf.status = "Отменен"
    else:
        trf.status = "Принят"
    trf.unloads = False
    pr = Product.objects.filter(traffic=trf)
    for ch in pr:
        ch.status = trf.status
        ch.dateUpload = datetime.now()
        ch.save()
    d1 = datetime.now()
    d2 = trf.dateUpload
    d2 = d2.replace(tzinfo=None)
    min = (d1 - d2).total_seconds() / 60
    min = int(min)
    trf.timeProc += min

    trf.save()
    return HttpResponse('', content_type='text/html')

def setRazgruzka2(request, id1):
    trf = Unloader.objects.get(id=id1)
    form = request.GET
    count = int(form["count"])
    i = 1
    while i <= count:
        car = Transport.objects.get(id= form["t" + str(i)])
        car.status = "Используется"
        car.dateEditStatus = datetime.now()
        car.unloadsTr = trf
        car.save()
        i += 1
    trf.status = "Загрузка"
    trf.loads = True
    trf.dateUpload = datetime.now()
    trf.save()
    return HttpResponse('', content_type='text/html')

def setRazgruzka(request, id1, id2):
    car = Transport.objects.get(id=id2)
    trf = Traffic.objects.get(id=id1)
    trf.unloads = True
    car.status = "Используется"
    car.dateEditStatus = datetime.now()
    car.unloads = trf
    car.save()
    trf.save()

    return HttpResponse('', content_type='text/html')


def startUnload(request, id1):
    tr = Unloader.objects.get(id=id1)
    tr.dateUpload = datetime.now()
    tr.status = "Загрузка"
    tr.loads = True
    tr.save()
    pr = Product.objects.filter(Unloader=tr)
    for ch in pr:
        ch.status = "Загрузка"
        ch.save()
    data = datetime.now()
    return HttpResponse(data, content_type='text/html')


def setPribil(request, id1):
    tr = Traffic.objects.get(id=id1)
    tr.dateUpload = datetime.now()
    tr.status = "Прибыл"
    tr.save()
    pr = Product.objects.filter(traffic=tr)
    for ch in pr:
        ch.status = "В обработке"
        ch.save()
    data = datetime.now()
    return HttpResponse(data, content_type='text/html')


def get_trafficU(request, id1):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    trU = Unloader.objects.get(id=id1)
    prd = Product.objects.filter(Unloader=trU)
    car = Transport.objects.filter(status="Простой")
    car2 = []
    for ch in car:
        d2 = ch.dateEditStatus
        d2 = d2.replace(tzinfo=None)
        if d2.day < datetime.now().day or d2.month < datetime.now().month:
            ch.allHoursUse += int(ch.timeUse / 60)
            ch.timeUse = 0
            ch.save()
        if ch.HoursDay / 60 < ch.HoursDay:
            car2.append(ch)
    car = car2
    try:
        car_now = Transport.objects.filter(unloadsTr=trU, status="Используется")[0]
    except Exception:
        car_now = ""
    data = {"index": 8, "us_name": us_name, "type_user": type_user, "tr": trU, "prd": prd, "car": car,
            "car_now": car_now}
    return render(request, "index1.html", context=data)


def get_traffic(request, id1):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    tr = Traffic.objects.get(id=id1)
    prd = Product.objects.filter(traffic=tr)
    car = Transport.objects.filter(status="Простой")
    car2 = []
    for ch in car:
        d2 = ch.dateEditStatus
        d2 = d2.replace(tzinfo=None)
        if d2.day < datetime.now().day or d2.month < datetime.now().month:
            ch.allHoursUse += int(ch.timeUse/60)
            ch.timeUse = 0
            ch.save()
        if ch.HoursDay / 60 < ch.HoursDay:
            car2.append(ch)
    car = car2
    try:
        car_now = Transport.objects.filter(unloads=tr, status="Используется")[0]
    except Exception:
        car_now = ""
    data = {"index": 5, "us_name": us_name, "type_user": type_user, "tr": tr, "prd": prd, "car": car,
            "car_now": car_now}
    return render(request, "index1.html", context=data)


def addNewEnd(request):
    form = request.GET
    name1 = form["traffic1"]
    typeProd = form["traffic3"]
    sklad = form["traffic5"]
    height = form["traffic10"]
    date1 = form["date"]
    sk = WarehouseSpace.objects.filter(name=sklad)[0]
    count = int(form["count"])
    i = 1
    allCount = 0
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    tr = Traffic.objects.create(name=name1, dateRegister=datetime.now(), sklad=sk, status="Отправлен",
                                dateArrival=date1)
    while i < count:
        nameProd = form["1t" + str(i)]
        tempure = form["2t" + str(i)]
        life = form["3t" + str(i)]
        countP = form["4t" + str(i)]
        allCount += int(countP)
        pr = Product.objects.create(name=nameProd, optimumTemperature=tempure, shelfLife=life,
                                    sklad=sk, traffic=tr, countPallet=countP, typeProduct=typeProd,
                                    status="Отправлен", height=height)
        pr.save()
        i += 1
    tr.coutPalletAll = allCount
    tr.save()
    return HttpResponse('', content_type='text/html')


def addNew1(request):
    form = request.GET
    date1 = form["date"]
    sklad = form["sklad"]
    print(date1)
    date = (datetime.strptime(date1, "%Y-%m-%d")).replace(tzinfo=None)
    sk = WarehouseSpace.objects.get(name=sklad)
    traf = Traffic.objects.filter(sklad=sk, dateArrival__gte=date).order_by("dateArrival")
    dateReturn = ""
    time_1Pallet = sk.secToPal
    ind = 0
    temp = 0
    if traf.count() == 0:
        dateReturn = date
    else:
        for car in traf:
            if car.dateArrival.day > date.day:
                dateReturn = date
                break
            temp = car
            ind += 1
            print("1)" + str(car.dateArrival))
        if ind >= 1:
            timeToThisCar = time_1Pallet * temp.coutPalletAll
            dateArr = temp.dateArrival + timedelta(seconds=timeToThisCar)
            print("2)" + str(dateArr))
            day = dateArr.day
            year = dateArr.year
            month = dateArr.month
            hour = dateArr.hour
            minute = dateArr.minute
            dateReturn = datetime(year, month, day, hour, minute, 0)
        print(dateReturn)
    return HttpResponse(dateReturn, content_type='text/html')


def addNewUnl(request):
    form = request.GET
    skName = form["sk"]
    arr = form["arr"]
    countPal = form["countPal"]
    arr = (datetime.strptime(arr, "%Y-%m-%d %H:%M:%S")).replace(tzinfo=None)
    i = 0
    un = Unloader.objects.create(dateRegister=datetime.now(), dateArrival=arr,
                                 status="Ожидание")
    countPp = 0
    while i < int(countPal):
        tov = form["t" + str(i)]
        tov = tov.replace("Tov", "")
        prd = Product.objects.get(id=tov)
        prd.status = "Загрузка"
        prd.Unloader = un
        prd.save()
        countPp += prd.countPallet
        i += 1
    un.coutPalletAll=countPp
    un.save()
    return HttpResponse("", content_type='text/html')


def getTime(request):
    form = request.GET
    date1 = form["date"]
    skName = form["sk"]
    date = (datetime.strptime(date1, "%Y-%m-%d")).replace(tzinfo=None)
    traf = Unloader.objects.filter(dateArrival__gte=date).order_by("dateArrival")
    sk = WarehouseSpace.objects.get(name=skName)
    dateReturn = ""
    skTo1Pallet = sk.secToPalZ

    ind = 0
    temp = 0
    if traf.count() == 0:
        dateReturn = date
    else:
        for car in traf:
            if car.dateArrival.day > date.day:
                dateReturn = date
                break
            temp = car
            ind += 1
        if ind >= 1:
            timeToThisCar = skTo1Pallet * temp.coutPalletAll
            dateArr = temp.dateArrival + timedelta(seconds=timeToThisCar)
            day = dateArr.day
            year = dateArr.year
            month = dateArr.month
            hour = dateArr.hour
            minute = dateArr.minute
            dateReturn = datetime(year, month, day, hour, minute, 0)
        print(dateReturn)

    return HttpResponse(dateReturn, content_type='text/html')


# 0.96
def addNew(request):
    form = request.GET
    countP = int(form["countP"])
    typeProd = form["traffic3"]
    min_temp = form["min"]
    max_height = form["traffic10"]
    sklad = WarehouseSpace.objects.filter(typeProduct=typeProd, optimumTemperature__lte=min_temp,
                                          shelving__height__gte=max_height)
    print(sklad)
    sk = {}
    in_=0
    for ch in sklad:
        oneYarus = ((ch.shelving.lengthS/100) * (ch.shelving.widthS/100)) / 100
        countPalOnYar = oneYarus / 0.96
        countOnOneSh = countPalOnYar * ch.shelving.countShelf
        countAll = int(ch.count * countOnOneSh)

        pr1 = Product.objects.filter(sklad=ch, status="Отправлен")
        pr2 = Product.objects.filter(sklad=ch, status="Прибыл")
        pr3 = Product.objects.filter(sklad=ch, status="Принят")
        batchall = 0
        for tov in pr1:
            batchall += int(tov.countPallet)
        for tov in pr2:
            batchall += int(tov.countPallet)
        for tov in pr3:
            batchall += int(tov.countPallet)
        onSklad = batchall + countP
        if onSklad <= countAll:
            sk["" + str(in_)] = ch.name
            in_+= 1
    sk["count"] = in_
    return JsonResponse(sk)


def unloading(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    prd = Product.objects.filter(status="Принят")
    wh = WarehouseSpace.objects.all()
    data = {"index": 7, "us_name": us_name, "type_user": type_user, "prd": prd, "countP": prd.count, "sk": wh}
    return render(request, "index1.html", context=data)


def show_index(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    tr = Traffic.objects.all().order_by("dateArrival")
    tr1 = Traffic.objects.filter(status="Отправлен")
    tr2 = Traffic.objects.filter(status="Прибыл")
    tr3 = Traffic.objects.filter(status="Принят")
    tr4 = Traffic.objects.filter(status="Отменен")
    tr5 = Unloader.objects.all()
    prd = Product.objects.all()
    data = {"index": 4, "us_name": us_name, "type_user": type_user, "tr": tr, "tr1": tr1,
            "tr2": tr2, "tr3": tr3, "tr4": tr4, "tr5": tr5, "prd": prd}
    return render(request, "index1.html", context=data)
