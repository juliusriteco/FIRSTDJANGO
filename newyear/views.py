from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request): #dit is de functie die laadt als er gevraagd wordt om 'index'. Zie urls.py
    now = datetime.now()
    
    return render(request, "newyear/index.html",{ #render het template genaamd index.html
        "date": now.month==9 and now.day == 16 #je krijgt er een variabele bij genaamd 'date'
    })