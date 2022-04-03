"""banks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.core.api import viewsets as listbanksviewset

route = routers.DefaultRouter()

route.register(r'books', listbanksviewset.listbanksViewSet, basename="Bancos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', include('core.urls', namespace='home')),
]