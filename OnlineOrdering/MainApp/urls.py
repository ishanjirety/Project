from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.log,name='log'),
    path('index',views.index,name='index'),
    path('store', views.store, name='store'),
    path('About', views.about, name='about'),
    path('Checkout', views.checkout, name='checkout'),
    path('reg', views.register, name='register'),
    path('registered', views.reg, name='reg'),
    path('login', views.loginValidation, name='loginValidation'),
    path('membership', views.membership, name='membership'),
    path('membershipreg', views.membership_reg, name='membership_reg'),
    path('donations', views.donations, name='donations'),
    path('logout', views.logout, name='logout'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('location',views.checkout,name="address"),
    
]