from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import showxml 
from wishlist.views import showjson
from wishlist.views import show_id_xml
from wishlist.views import show_id_json
from wishlist.views import register 
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import create
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('xml/<int:id>', show_id_xml, name='show_id_xml'),
    path('json/<int:id>', show_id_json, name='show_id_json'),  
    path('xml/', showxml, name='showxml'),
    path('json/', showjson, name='showjson'),
    path('', show_wishlist, name='show_wishlist'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/submit/', create, name='tbl-form'),
]