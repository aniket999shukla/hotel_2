from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request): 
    return render(request, "index.html")

def book(request): 
    return render(request, "book_room.html")

def payment(request): 
    return render(request, "payment.html")

def signup(request): 
    return render(request, "signup.html")

def feedback(request): 
    return render(request, "feedback.html")

def event(request): 
    return render(request, "event.html")

def register(request): 
    return render(request, "register.html")

def refund(request): 
    return render(request, "refund.html")

def discount(request): 
    return render(request, "discount.html")

