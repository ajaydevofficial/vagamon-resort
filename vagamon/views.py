from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from booking.models import booking

def home_page(request):
    context = {}
    return render(request,"index.html",context)

def tour_page(request):
    context = {}
    return render(request,"tour.html",context)

def login_page(request):
    context = {}
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if not user==None:
            login(request,user)
            return redirect(home_page)
        else:
            print("Login Failed")
            return render(request,"login.html",{"invalid":True})
    return render(request,"login.html",context)

def book_page(request):
    context = {}
    if request.method =='POST':
        print(request.POST)
    return render(request,"book.html",context)

def admin_page(request):
    context = {}
    if request.method == 'POST':
        package = request.POST['package-type']
        inDate = request.POST['in-date']
        outDate = request.POST['out-date']
        print(package)
        print(inDate)
        print(outDate)
        booking.objects.create(package=package,inDate=inDate,outDate=outDate)
        return redirect(home_page)
    return render(request,"admin.html",context)
