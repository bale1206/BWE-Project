from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explorer', views.explorer, name='explorer'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('plans', views.plans, name='plans'),
]

