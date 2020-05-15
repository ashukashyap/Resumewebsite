from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('exprince',views.Exprince,name='Exprince'),
    path('edu',views.Edu , name="Edu"),
    path('skils',views.Skils , name="Skils"),
    path('contact',views.contact , name="Contact"),
]
