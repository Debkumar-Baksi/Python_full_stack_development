from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def index(request):
    return HttpResponse("<h1>Hello There</h1>")


def home(request):
    return render(request,'accounts/home.html')


def date_time(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))

    if h<12:
        msg="Good Morning "
    elif h<16:
        msg="Good Afternoon"
    elif h<21:
        msg="Good Evening"
    else:
        msg="Good Night"

    my_dict={'date':date , 'msg':msg}
    return render(request,'accounts/home.html',my_dict)