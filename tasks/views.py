from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render




class NewTaskForm(forms.Form):#functie die een field maakt
    task = forms.CharField(label="New Task") #maak een input field met characters
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5, initial=3) #maak een input field met integers

# Create your views here.

def index(request): #'index' pagina template, variabele & functies
    if "tasks" not in request.session:
        request.session["tasks"] =[] #lijst teruggeven voor in lokale sessie
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request): #'add' pagina template, variabele & functies
    if request.method == "POST":
        form = NewTaskForm(request.POST) #stopt de input van gebruiker van Form in variabele
        if form.is_valid(): #belangrijk voor server side validation (als nog niet gerefreshed is bijv. )
            task = form.cleaned_data["task"] #maakt variabele aan met data van inputfield: 'task' uit form
            request.session["tasks"] += [task] #append, maar dan in lokale sessie 
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks.add.html", { 
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm(), #functie die een form maakt -> Genaamd form
    })