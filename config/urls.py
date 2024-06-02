from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from orders.views import stripe_webhook_view

urlpatterns = [
    path("", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("webhook/stripe/", stripe_webhook_view, name="stripe_webhook"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)