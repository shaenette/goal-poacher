from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Football Shop",
        "student_name": "Nazwa Zahra Sausan",
        "class_name": "PBP D",
    }
    return render(request, "main.html", context)

