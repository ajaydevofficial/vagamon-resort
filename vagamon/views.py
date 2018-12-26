from django.shortcuts import render,redirect

def home_page(request):
    context = {}
    return render(request,"index.html",context)

def tour_page(request):
    context = {}
    return render(request,"tour.html",context)

def book_page(request):
    context = {}
    if request.method=='POST':
        print(request.POST)
    return render(request,"book.html",context)
