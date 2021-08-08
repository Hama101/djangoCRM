from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


def home(request):
    print("1")
    customers = Customer.objects.all()
    print("2")
    orders = Order.objects.all()
    print("3")
    total_customers = customers.count()
    print("4")
    total_orders = orders.count()
    print("5")
    delivered = orders.filter(status='Delivered').count()
    print("6")
    pending = orders.filter(status='Pending').count()
    print("7")

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending , 
        }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()  # Import the database of product
    # dict:what we need to call in the template
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk_test2):
    order = Order.objects.get(id=pk_test2)
    form = OrderForm(request.POST or None , instance=order)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

#it s hamma
def deleteOrder(request , pk_test2):
    order = Order.objects.get(id=pk_test2)
    order.delete()
    return redirect('/')