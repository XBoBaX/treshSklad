from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from products import views as prd_views
from WarehouseSpace import views as skld_views
from shelving import views as shelv_views
from traffic import views as traf_views
from transport import views as car_views
from stats import views as sts_views
urlpatterns = [
    path('',  prd_views.show_index),
    path('sklad/add/', skld_views.add_sklad),
    path('sklad/', skld_views.show_index),
    path('shelving/add/', shelv_views.add_stelag),
    path('shelving/', shelv_views.show_index),
    path('traffic/addNew/end', traf_views.addNewEnd),
    path('traffic/addNew/1', traf_views.addNew1),
    path('traffic/addNew/', traf_views.addNew),
    path('traffic/unloading/', traf_views.unloading),
    path('traffic/unloading/addNew/', traf_views.addNewUnl),
    path('traffic/unloading/getTime/', traf_views.getTime),
    path('traffic/', traf_views.show_index),
    re_path(r'traffic/setPribil/(?P<id1>.+)/', traf_views.setPribil),
    re_path(r'traffic/startUnload/(?P<id1>.+)/', traf_views.startUnload),
    re_path(r'traffic/setRazgruzkaU/(?P<id1>.+)/', traf_views.setRazgruzka2),
    re_path(r'traffic/setRazgruzka/(?P<id1>.+)/(?P<id2>.+)/', traf_views.setRazgruzka),
    re_path(r'traffic/stopTraffic3/(?P<id1>.+)/', traf_views.stopTraffic3),
    re_path(r'traffic/stopTraffic2/(?P<id1>.+)/(?P<id3>.+)/', traf_views.stopTraffic2),
    re_path(r'traffic/stopTraffic/(?P<id1>.+)/(?P<id3>.+)/', traf_views.stopTraffic),
    re_path(r'traffic/editU/(?P<id1>.+)/', traf_views.get_trafficU),
    re_path(r'traffic/edit/(?P<id1>.+)/', traf_views.get_traffic),
    path('traffic/', traf_views.show_index),
    path('car/add/', car_views.add_car),
    path('car/', car_views.show_index),
    path('stats/get/', sts_views.getSt),
    path('stats/', sts_views.show_index),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

