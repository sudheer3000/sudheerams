from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("customerlogin",views.customerlogin,name="customerlogin"),
    path("mechaniclogin",views.mechaniclogin,name="mechaniclogin.html"),
    path("aboutus",views.aboutus,name="aboutus.html")
]