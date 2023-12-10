from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    products_count = products.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            instance=order_form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        order_form = OrderForm()
    context = {
        'orders':orders,
        'order_form': order_form,
        'products': products,
        'orders_count': orders_count,
        'products_count':products_count,
        'workers_count':workers_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    orders_count = Order.objects.all().count()
    products_count = Product.objects.all().count()
    workers_count = workers.count()
    context = {
        'workers':workers,
        'orders_count': orders_count,
        'products_count': products_count,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }

    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    items = Product.objects.all()
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    orders_count = Order.objects.all().count()
    products_count = items.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            product_name = product_form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            redirect('dashboard-product')
    else:
        product_form = ProductForm()
    context = {
        'items': items,
        'product_form':product_form,
        'orders_count':orders_count,
        'workers_count': workers_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES ,instance=item)
        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard-product')
    else:
        product_form = ProductForm(instance=item)

    context={
        'product_form':product_form
    }

    return render(request, 'dashboard/product_edit.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    context = {
        'orders':orders,
        'orders_count':orders_count,
        'products_count':products_count,
        'workers_count':workers_count,
    }
    return render(request, 'dashboard/order.html', context)
