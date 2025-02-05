from django.db import models
from django.contrib.auth.models import AbstractUser

# Выбор статуса заказа
STATE_CHOICES = (
    ('basket', 'Статус корзины'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)

# Выбор типа пользователя
USER_TYPE_CHOICES = (
    ('shop', 'Магазин'),
    ('buyer', 'Покупатель'),
)


# Модель пользователя
class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=5, choices=USER_TYPE_CHOICES, default='buyer')

    def __str__(self):
        return self.email


# Модель магазина
class Shop(models.Model):
    """Модель магазина."""
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='Пользователь',
                                blank=True, null=True,
                                on_delete=models.CASCADE)
    state = models.BooleanField(verbose_name='статус получения заказов', default=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Список магазинов"
        ordering = ('-name',)

    def __str__(self):
        return self.name


# Модель категории
class Category(models.Model):
    """Модель категории товаров."""
    name = models.CharField(max_length=40, verbose_name='Название')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины', related_name='categories', blank=True)

    def __str__(self):
        return self.name


# Модель продукта
class Product(models.Model):
    """Модель продукта."""
    name = models.CharField(max_length=80, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Модель информации о продукте
class ProductInfo(models.Model):
    """Модель информации о продукте."""
    model = models.CharField(max_length=80, verbose_name='Модель', blank=True)  # Поле для модели продукта
    external_id = models.PositiveIntegerField(verbose_name='Внешний ИД')  # Поле для внешнего идентификатора
    product = models.ForeignKey(Product, verbose_name='Продукт', related_name='product_infos', blank=True,
                                on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='product_infos', blank=True,
                             on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')  # Поле для количества
    price = models.PositiveIntegerField(verbose_name='Цена')  # Поле для цены
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')  # Поле для рекомендованной цены

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = "Информационный список о продуктах"
        constraints = [
            models.UniqueConstraint(fields=['product', 'shop', 'external_id'], name='unique_product_info'),
        ]


# Модель параметра
class Parameter(models.Model):
    """Модель параметра продукта."""
    name = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self):
        return self.name


# Модель параметра продукта
class ProductParameter(models.Model):
    """Модель параметра продукта."""
    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о продукте', related_name='product_parameters', on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name='Параметр', related_name='product_parameters', on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=100)

    def __str__(self):
        return f'{self.parameter.name}: {self.value}'


# Модель контакта
class Contact(models.Model):
    """Модель контактов пользователя."""
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='contacts', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=15, verbose_name='Дом', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house}'


# Модель заказа
class Order(models.Model):
    """Модель заказа."""
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='orders', on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now_add=True)
    state = models.CharField(verbose_name='Статус', choices=STATE_CHOICES, max_length=15)
    contact = models.ForeignKey(Contact, verbose_name='Контакт', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Список заказов"
        ordering = ('-dt',)

    def __str__(self):
        return f'Заказ {self.id} от {self.dt}'


# Модель позиции заказа
class OrderItem(models.Model):
    """Модель позиции заказа."""
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='ordered_items', on_delete=models.CASCADE)
    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о продукте', related_name='ordered_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product_info.product.name} - {self.quantity}'
