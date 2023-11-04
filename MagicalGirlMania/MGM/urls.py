from django.urls import path
from MGM import views

urlpatterns = [
    #Vista inicio (acá también va a estar el buscador GET)
    path('', views.index, name="index"),
    #Vista crear Winx
    path('winx/', views.winx, name="winx"),
    #Vista crear Witch
    path('witch/', views.witch, name="witch"),
    #Vista crear Sailor
    path('sailor/', views.sailor, name="sailor"),
    
    #URLs de los Form
    path('sailorForm/', views.sailorForm, name='sailorForm'),
    path('winxForm/', views.winxForm, name='winxForm'),
    path('witchForm/', views.witchForm, name='witchForm'),
]
