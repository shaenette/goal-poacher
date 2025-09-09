from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Football Shop",
        "student_name": "Shaen Cliantha",
        "class_name": "PBP Kelas A",
    }
    return render(request, "main.html", context)

