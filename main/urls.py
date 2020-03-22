from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('', main_entry_point, name = 'main_entry_point'),
    path('suppliers', suppliers, name = 'suppliers'),
    path('points', points, name = 'points'),
    path('new_sup', new_supplier, name = 'new_sup'),
    
]

