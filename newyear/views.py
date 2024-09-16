from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.now()
    
    return render(request, "newyear/index.html",{
        "date": now.month==9 and now.day == 16
    })