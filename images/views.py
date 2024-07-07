from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if image_file:
            # Save the image to your server
            # Change the path according to your requirements
            image_path = 'D:/TrackLive Backend Django/djangorest/media/' + image_file.name

            with open(image_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
            # Return the image path 
            # return Response({'image_path': image_path}, status=200)
            return Response({'image_path': image_file.name}, status=200)
        else:
            return Response({'error': 'No image found'}, status=400)
        


from django.http import HttpResponse, FileResponse
from django.conf import settings
import os

class ImageServeView(APIView):
    def get(self, request, image_name):
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        if os.path.exists(image_path):
            print(image_path)
            img = open(image_path, 'rb')
            print(img)
            return HttpResponse(img, content_type="image/jpg")
            # with open(image_path, 'rb') as img:
            #     return HttpResponse(img.read(), content_type="image/jpeg")
        else:
            return Response({'error': 'Image not found'}, status=400)

# http://192.168.0.110:8000/image/get/Profile.png/