from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import showxml 
#sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import showjson
from wishlist.views import show_id_xml
from wishlist.views import show_id_json

app_name = 'wishlist'

urlpatterns = [
    path('xml/<int:id>', show_id_xml, name='show_id_xml'),
    path('json/<int:id>', show_id_json, name='show_id_json'),  
    path('xml/', showxml, name='showxml'),
    path('json/', showjson, name='showjson'),
    path('', show_wishlist, name='show_wishlist')
]