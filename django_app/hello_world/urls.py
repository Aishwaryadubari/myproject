from django.urls import path
from . import views  #importing our view file

urlpatterns = [
    path('<int:pk>/', views.car_detail, name="car_detail"),
    path('', views.showdata,name="showdata"),
    path('insert/',views.insertemp,name="insertemp"),
]