from django.urls import path, include


from rest_framework.routers import DefaultRouter

from .views import UserViewSet, GroupViewSet
# create router object
router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename= 'group') 
# companies/{id}/employees/

router.register(r'users', UserViewSet , basename='user') 

urlpatterns = [
    path('', include(router.urls)),
]

