from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index") #in het pad "", index functie in view laden, naam is "index"
]