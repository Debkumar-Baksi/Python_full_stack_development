from django.urls import path
from . import views
urlpatterns=[

    path('',views.home,name='home'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('product/',views.product,name='product'),
    path('create_order/',views.createorder,name='create_order'),
    path('update_order/<str:pk>/',views.updateorder,name='update_order')
]