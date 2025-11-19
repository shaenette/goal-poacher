import datetime
import requests
import json
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

#=====LOGIN REGISTER FUNCTION=====
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 Account created successfully! Please login.')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, f'👋 Welcome back, {user.username}!')
            return response
      else:
            messages.error(request, '❌ Invalid username or password.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.info(request, '👋 You have successfully logged out.')
    return response

#=====SHOWING PRODUCTS======
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        "app_name": "Goal Poacher",
        "username": request.user.username,
        "student_name": "Nazwa Zahra Sausan",
        "class_name": "PBP D",
        "npm": "2406397750",
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        form.save()
        messages.success(request, '🛒 Product added successfully!')
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.info(request, '✏️ Product has been updated successfully.')
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    messages.warning(request, '🗑 Product has been deleted.')
    return HttpResponseRedirect(reverse('main:show_main'))

#=====XML & JSON=====
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    qs = Product.objects.all().select_related('user')
    data = [{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'thumbnail': p.thumbnail,
        'category': p.category,
        'is_featured': p.is_featured,
        'stock': p.stock,
        'user_id': p.user_id,
        'user_username': p.user.username if p.user else None,
    } for p in qs]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
     try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'stock': product.stock,
        'user_id': product.user_id,
        'user_username': product.user.username if product.user else None
        }
        return JsonResponse(data)
     except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        price = data.get("price", 0)
        description = strip_tags(data.get("description", ""))
        thumbnail = data.get("thumbnail", "")
        category = data.get("category", "others")
        is_featured = data.get("is_featured", False)
        stock = data.get("stock", 0)

        user = request.user if request.user.is_authenticated else None

        product = Product.objects.create(
            user=user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
        )

        return JsonResponse({
            "status": "success",
            "id": product.id,
            "message": "Product created"
        }, status=201)

    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
