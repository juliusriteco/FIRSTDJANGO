from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"), #in het pad "", index functie in view laden, naam is "index"
    path("add", views.add, name="add"), #in het pad "", index functie in view laden, naam is "index"
]