from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Que traiga también los urls de la app MGM
    path('', include('MGM.urls')),
]
