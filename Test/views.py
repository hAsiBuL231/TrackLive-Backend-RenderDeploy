from django.shortcuts import render

# Create your views here.
#views.py

from . import models
from django.shortcuts import render

def test(request):
    return render(request, 'test.html', context = {}) 