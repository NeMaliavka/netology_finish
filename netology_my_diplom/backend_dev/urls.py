from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ShopViewSet, CategoryViewSet, ProductViewSet, ProductInfoViewSet, ContactViewSet, OrderViewSet, OrderItemViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


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
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
