from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# render is used to respond a html page
# Create your views here.
def home(request):
    return render(request, "home.html")


def adminlogin(request):
    return render(request, "adminlogin.html")


def customerlogin(request):
    return render(request, "customerlogin.html")


def mechaniclogin(request):
    return render(request, "mechaniclogin.html")


def aboutus(request):
    return render(request, "aboutus.html")


from django.shortcuts import render

# Create your views here.
