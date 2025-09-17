from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from .models import Employee

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()

    context = {
        "app_name": "Football Shop",
        "student_name": "Nazwa Zahra Sausan",
        "class_name": "PBP D",
        'product_list' : product_list,
    }
    return render(request, "main.html", context)

def create_employee(request):
    employee = Employee.object.create(name="Nazwa Zahra Sausan", age=19, persona="ajbdja")
    return HttpResponse(f"Ini me-return {employee.name}")

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
     product_list = Product.objects.all()
     json_data = serializers.serialize("json", product_list)
     return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
     try:
        product = Product.objects.filter(pk=id)
        json_data = serializers.serialize("json", product)
        return HttpResponse(json_data, content_type="application/json")
     except Product.DoesNotExist:
        return HttpResponse(status=404)
