from django.shortcuts import render
from .models import Product , Customer , Order , Tag

# Create your views here.
def home(request):
    orders=Order.objects.all()
   

    total_order=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,
             'total_order':total_order,
             'delivered':delivered,
             'pending':pending}

    return render(request,'accounts/dashboard.html',context)



def Product(request):
    return render(request,'accounts/product.html') 




def Customer(request):
    return render(request,'accounts/customer.html')
