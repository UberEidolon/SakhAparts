from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "index.html")

# def list(request):
#     items = ListItem.objects.all()
#     return render(request, "html/list.html", {"list": items})
