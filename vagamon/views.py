from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from booking.models import booking
from review.models import review
from django.contrib.auth import logout
from booking_count.models import booking_count
import datetime

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
        ind = request.POST['individuals']
        request.session['package'] = package
        request.session['inDate'] = inDate
        request.session['outDate'] = outDate
        request.session['ind'] = ind
        try:
            qs = booking.objects.get(package=package,inDate=inDate,outDate=outDate)
            if qs:
                return render(request,"book.html",{"exists":True})
            else:
                return redirect(checkout_page)
        except:
            return redirect(checkout_page)
    return render(request,"book.html",context)

def admin_page(request):
    context = {}
    count_obj = booking_count.objects.all()
    try:
        count = count_obj.values_list('count',flat=True)[0]
    except:
        pass
    if request.method == 'POST':
        package = request.POST['package-type']
        inDate = request.POST['in-date']
        outDate = request.POST['out-date']
        status = request.POST['status']
        individuals = request.POST['individuals']
        count = count+1
        booking.objects.create(package=package,inDate=inDate,outDate=outDate,status=status,individuals=individuals,booking_id=count)
        booking_count.objects.filter().update(count=count)
        return render(request,"admin.html",{"success":True})
    return render(request,"admin.html",context)

def logout_page(request):
    logout(request)
    return redirect(home_page)

def checkout_page(request):
    base = 0
    try:
        package = request.session['package']
        if package == "Cottage and Food":
            base = 1000
        elif package =='Other':
            base = 2000
        ind = int(request.session['ind'])
        inDate = datetime.datetime.strptime(request.session['inDate'], "%Y-%m-%d").date()
        outDate = datetime.datetime.strptime(request.session['outDate'], "%Y-%m-%d").date()
        day = (outDate-inDate).days

        if day ==0:
            day =1
        amount = ind*day*base
        amount_view = "Pay Rs."+str(amount)
        context = {"amount_view":amount_view,"inDate":inDate,"outDate":outDate,"ind":ind,"package":package,"Break" : False,"amount":amount}


        return render(request,"checkout.html",context)
    except:
        return render(request,"checkout.html",{"Break" : True})
