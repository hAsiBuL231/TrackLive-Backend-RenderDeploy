from django.urls import path
from .views import ImageUploadView, ImageServeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('get/<str:image_name>/', ImageServeView.as_view(), name='image-serve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
