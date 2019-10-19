from django.shortcuts import render
from django.contrib import auth
from Profile.models import Profile
from .models import Shelving
from django.http import HttpResponse

def add_stelag(request):
    stelag_height = request.GET.get('stelag_height', '')
    stelag_heightlengthS = request.GET.get('stelag_dlina', '')
    stelag_widthS = request.GET.get('stelag_shirina', '')
    stelag_countShelf = request.GET.get('stelag_count', '')
    stelag_kg_polki = request.GET.get('stelag_kg', '')

    stelag = Shelving.objects.create(height=stelag_height, lengthS=stelag_heightlengthS,
                                    widthS=stelag_widthS, countShelf=stelag_countShelf,
                                    kg_polki=stelag_kg_polki)
    stelag.save()

    return HttpResponse('yea', content_type='text/html')

def show_index(request):
    type_user = "Грузчик"
    us_name = "1"
    if auth.get_user(request).username.__len__() > 0:
        us_name = auth.get_user(request).username
        us_name = us_name[:10]
        profile = Profile.objects.get(user=auth.get_user(request))
        type_user = profile.position
    stelag = Shelving.objects.all()

    data = {"index": 3, "us_name": us_name, "type_user": type_user,
            "stelag": stelag}
    return render(request, "index1.html", context=data)

