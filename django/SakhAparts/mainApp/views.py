from django.shortcuts import render, HttpResponse
from .models import ListItem

# Create your views here.


def home(request):
    return render(request, "html/home.html")

def list(request):
    items = ListItem.objects.all()
    return render(request, "html/list.html", {"list": items})