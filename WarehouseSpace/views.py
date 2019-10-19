from django.shortcuts import render
from django.contrib import auth
from Profile.models import Profile
from .models import WarehouseSpace
from shelving.models import Shelving
from django.http import HttpResponse

def add_sklad(request):
    sklad_name = request.GET.get('sklad_name', '')
    sklad_visota = request.GET.get('sklad_visota', '')
    sklad_ploshad = request.GET.get('sklad_ploshad', '')
    sklad_temp = request.GET.get('sklad_temp', '')
    sklad_type_Stelash = request.GET.get('sklad_type_Stelash', '')
    count_st = request.GET.get('sklad__count_st', '')
    sklad_type = request.GET.get('sklad_type', '')

    stelash = Shelving.objects.get(id=sklad_type_Stelash)
    sklad = WarehouseSpace.objects.create(name=sklad_name, height=sklad_visota,
                                          size=sklad_ploshad,
                                          optimumTemperature=sklad_temp,
                                          shelving = stelash, count=count_st,
                                          typeProduct=sklad_type)
    sklad.save()

    return HttpResponse('yea', content_type='text/html')

def show_index(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        us_name = us_name[:10]
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    sklad = WarehouseSpace.objects.all()
    skladSyx = WarehouseSpace.objects.filter(typeProduct="Сухие товары")
    skladSkr = WarehouseSpace.objects.filter(typeProduct="Скоропортящиеся товары")
    skladXry = WarehouseSpace.objects.filter(typeProduct="Хрупкие товары")
    stelagi = Shelving.objects.all()

    data = {"index": 2, "us_name": us_name, "type_user": type_user, "sklad": sklad,
            "skladSkr": skladSkr, "skladSyx": skladSyx, "skladXry": skladXry,
            "stelagi": stelagi}
    return render(request, "index1.html", context=data)

