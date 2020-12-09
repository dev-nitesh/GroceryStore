from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products, name= 'products'),
    path('bread', views.bread, name= 'bread'),
    path('drinks', views.drinks, name= 'drinks'),
    path('frozen', views.frozen, name= 'frozen'),
    path('household', views.household, name= 'household'),
    path('kitchen', views.kitchen, name= 'kitchen'),
    path('pet', views.pet, name= 'pet'),
    path('vegetables', views.vegetables, name= 'vegetables'),
] 