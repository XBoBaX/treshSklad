from django.shortcuts import render
from django.contrib import auth
from Profile.models import Profile
from products.models import Product
from WarehouseSpace.models import WarehouseSpace

def show_index(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        us_name = us_name[:10]
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    prd = Product.objects.all()
    prd_sx = Product.objects.filter(status="Отправлен").count()
    prd_st = Product.objects.filter(status="В обработке").count()
    prd_ht = Product.objects.filter(status="Принят").count()
    prd_ot = Product.objects.filter(status="Отменен").count()
    sklad = WarehouseSpace.objects.all()
    data = {"index": 1, "us_name": us_name, "type_user": type_user, "prd": prd,
            "prd_sx": prd_sx, "prd_st": prd_st, "prd_ht": prd_ht, "prd_ot": prd_ot,
            "sk": sklad}
    return render(request, "index1.html", context=data)


