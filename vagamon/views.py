from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from booking.models import booking
from review.models import review
from django.contrib.auth import logout

def home_page(request):
    context = {}
    try:
        reviews_view  = review.objects.raw("SELECT * from review_review")
        context = {"reviews":reviews_view}
    except:
        pass

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['something']
        rating = int(request.POST["rating"])
        code = ""
        for i in range(0,rating):
            code = code + '★'
        review.objects.create(name=name,email=email,phone=phone,text=text,rating=rating,code=code)
        context = {"reviews":reviews_view,"success":True}
        return render(request,"index.html",context)

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
        package = request.POST['package-type']
        inDate = request.POST['in-date']
        outDate = request.POST['out-date']
        try:
            qs = booking.objects.get(package=package,inDate=inDate,outDate=outDate)
            if qs:
                return render(request,"book.html",{"exists":True})
            else:
                return render(request,"checkout.html",{"package":package,"inDate": inDate,"outDate": outDate})
        except:
            return render(request,"checkout.html",{"package":package,"inDate": inDate,"outDate": outDate})
    return render(request,"book.html",context)

def admin_page(request):
    context = {}
    if request.method == 'POST':
        package = request.POST['package-type']
        inDate = request.POST['in-date']
        outDate = request.POST['out-date']
        status = request.POST['status']
        individuals = request.POST['individuals']
        booking.objects.create(package=package,inDate=inDate,outDate=outDate,status=status,individuals=individuals)
        return render(request,"admin.html",{"success":True})
    return render(request,"admin.html",context)

def logout_page(request):
    logout(request)
    return redirect(home_page)
