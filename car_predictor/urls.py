from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_car_price, name='predict_car_price'),
]
