from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path('', index),  
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
