"""
URL configuration for djangorest project.

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
from django.urls import path
from django.urls import include


from rest_framework import routers

from api.views import UserViewSet, GroupViewSet
from authentication.View_login import LoginView
from authentication.View_register import RegistrationView
from locations.views import LocationViewSet
from sos_history.views import SOSHistoryViewSet

router = routers.DefaultRouter()
# router.register(r'register', RegistrationView.as_view()) 
# router.register(r'login', LoginView.as_view()) 

router.register(r'groups', GroupViewSet) 
# companies/{id}/employees/

router.register(r'users', UserViewSet) 
router.register(r'locations', LocationViewSet)
router.register(r'soshistory', SOSHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('test/', include('Test.urls')),
    path('image/', include('images.urls')),

    path('', include(router.urls)),  # Include the router's URL patterns for the notes app

    # path('api/', include('api.urls')),
    # path('location/', include('locations.urls')),
]
