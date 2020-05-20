"""canteenmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from user.views import UserViewSet


router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('user.urls')),
    path('api/menu/', include('menu.urls')),
    # path('api/breakfast/', include('breakfast.urls')),
    # path('api/today-special/', include('today_special.urls')),
    # path('api/snacks/', include('snacks.urls')),
    # path('api/dinner/', include('dinner.urls')),
    # path('api/lunch/', include('lunch.urls')),
    path('api/invoice/', include('invoice.urls')),
]
