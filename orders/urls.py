from django.urls import path
from .views import OrderCreateView, SuccessTemplateView, CancelTemplateView, OrderListView, OrderDetailView

app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancel/', CancelTemplateView.as_view(), name='order_cancel'),
]