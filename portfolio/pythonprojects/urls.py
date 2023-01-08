from django.urls import path
from . import views

urlpatterns = [path("", views.py_proj, name="pyproj"), path("dad_jokes", views.py_jokes, name="dadjokes")]
