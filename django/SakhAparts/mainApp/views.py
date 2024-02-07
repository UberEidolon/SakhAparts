from django.shortcuts import render, HttpResponse
from .models import Apartment


def home(request):
    items = Apartment.objects.all()
    return render(request, "index.html", {"list": items})
