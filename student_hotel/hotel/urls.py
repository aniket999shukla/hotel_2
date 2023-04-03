from django.contrib import admin
from django.urls import include, path
from hotel import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book', views.book, name="book"),
    path('payment', views.payment, name="payment"),
    path('signup', views.signup, name="signup"),
    path('feedback', views.feedback, name="feedback"),
    path('event', views.event, name="events"),
    path('register', views.register, name="register"),
    path('refund', views.refund, name="refund"),
    path('discount', views.discount, name="discount")
    
]