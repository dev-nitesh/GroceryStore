from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    #path('login', views.login, name= 'login'),
    path('', views.output, name= 'output'),
    path('<int:id>', views.user_details, name= 'user_details'),
] 