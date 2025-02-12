from django.shortcuts import render
from .models import Product , Customer , Order , Tag

# Create your views here.
def home(request):
    orders=Order.objects.all()
    customers = Customer.objects.all()

    total_order=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,
             'customers': customers,
             'total_order':total_order,
             'delivered':delivered,
             'pending':pending}

    return render(request,'accounts/dashboard.html',context)



def product(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'accounts/product.html',context) 




def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customer.html', context)
