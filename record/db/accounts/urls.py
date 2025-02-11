from django.urls import path
from . import views
urlpatterns=[

    path('',views.home,name='home'),
    path('customer',views.Customer,name='customer'),
    path('product',views.Product,name='product'),
]