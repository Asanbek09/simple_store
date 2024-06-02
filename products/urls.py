from django.urls import path
from .views import IndexView, ProductsListView
from . import views

app_name = "products"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
]