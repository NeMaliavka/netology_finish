from rest_framework import viewsets
from .models import User, Shop, Category, Product, ProductInfo, Contact, Order, OrderItem
from .serializers import UserSerializer, ShopSerializer, CategorySerializer, ProductSerializer, ProductInfoSerializer, ContactSerializer, OrderSerializer, OrderItemSerializer

from .utils import send_invoice_email
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.cache import cache


def my_view(request):
    data = cache.get('my_data')
    if not data:
        data = expensive_query()  # Ваша функция для получения данных
        cache.set('my_data', data, timeout=60*15)  # Кэшировать на 15 минут
    return JsonResponse(data)


def fulfill_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.state = 'confirmed'
    order.save()
    send_invoice_email_task.delay(order.id)  # Асинхронный вызов
    return JsonResponse({'status': 'success', 'message': 'Заказ исполнен и накладная отправлена.'})

# ViewSet для пользователя
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet для магазина
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# ViewSet для категории
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ViewSet для продукта
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ViewSet для информации о продукте
class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


# ViewSet для контактов
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# ViewSet для заказов
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ViewSet для позиций заказа
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
