"""
URL configuration for imtihon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from mainapp.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("haydovchilar", HaydovchilarModelViewSet)
router.register("buyurtmalar", BuyurtmalarModelViewSet)
router.register("mijozlar", MijozlarAPI)
router.register("adminlar", AdminlarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPI.as_view()),
    path('suv/<int:son>/', SuvAPI.as_view()),
    path('mijoz/<int:son>/', MijozAPI.as_view()),
    path('admins/<int:son>/', AdminAPI.as_view()),
    path('', include(router.urls)),
]
