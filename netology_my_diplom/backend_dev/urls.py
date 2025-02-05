from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ShopViewSet, CategoryViewSet, ProductViewSet, ProductInfoViewSet, ContactViewSet, OrderViewSet, OrderItemViewSet

# Создаем маршрутизатор
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_info', ProductInfoViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)

# Определяем URL-адреса
urlpatterns = [
    path('', include(router.urls)),
]
