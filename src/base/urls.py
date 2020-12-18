from django.urls import path

from .views import HomeView, OrderDetailView, OrderPizza

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('orders/<pk>/', OrderDetailView.as_view(), name="order_details"),
    path('api/order/', OrderPizza.as_view())
]
