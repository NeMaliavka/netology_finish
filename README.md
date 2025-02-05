# Netology My Diplom

## Описание проекта

**Netology My Diplom** — это веб-приложение, разработанное на Django, которое позволяет пользователям управлять магазинами, категориями продуктов, заказами и контактной информацией. Приложение включает в себя функции отправки уведомлений по электронной почте и управления заказами.

## Установка

### Предварительные требования

- Python 3.8 или выше
- Django 4.0 или выше
- pip

### Клонирование репозитория
git clone https://github.com/ваш-логин/netology_my_diplom.git

cd netology_my_diplom

### Установка зависимостей
Создайте виртуальное окружение и активируйте его:

python -m venv venv

source venv/bin/activate  # Для Linux/Mac

venv\Scripts\activate  # Для Windows


#### Установите зависимости:

pip install -r requirements.txt

### Настройка базы данных

Настройте параметры подключения в файле netology_my_diplom/settings.py.

#### Миграции
Примените миграции для создания необходимых таблиц в базе данных:

python manage.py migrate

#### Создание суперпользователя
Создайте суперпользователя для доступа к админке:

python manage.py createsuperuser

#### Запуск сервера
Запустите сервер разработки:

python manage.py runserver

Теперь Вы можете получить доступ к приложению по адресу http://127.0.0.1:8000/.

### Использование
#### Основные функции
- Управление магазинами: Добавление, редактирование и удаление магазинов.
- Управление категориями: Создание и связывание категорий с магазинами.
- Управление продуктами: Добавление продуктов в категории.
- Управление заказами: Создание, редактирование и выполнение заказов.
- Контактная информация: Добавление и управление контактами пользователей.
- Отправка уведомлений: Автоматическая отправка уведомлений по электронной почте при создании заказов.
API
- Проект также предоставляет API для взаимодействия с приложением. Вы можете использовать инструменты, такие как Postman, для тестирования API.

#### Примеры запросов
- Создание заказа:

POST /api/orders/

Content-Type: application/json

{
    "user": 1,
    "state": "new",
    "contact": 1
}

- Получение списка заказов:

GET /api/orders/

- Тестирование

Для запуска тестов почтовых отправлений используйте pytest. Убедитесь, что у Вас установлены все зависимости.

pytest

### База Данных
#### Скрипт, который был использован для заполнения БД, через Shell:
from backend_dev.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Contact, Order, OrderItem
- Создание пользователей:

user1 = User.objects.create_user(email="shop1@example.com", password="password123", first_name="Магазин", last_name="Первый", type="shop")

user2 = User.objects.create_user(email="shop2@example.com", password="password123", first_name="Магазин", last_name="Второй", type="shop")
- Создание магазинов:

shop1 = Shop.objects.create(name="Магазин 1", url="http://shop1.com", user=user1)

shop2 = Shop.objects.create(name="Магазин 2", url="http://shop2.com", user=user2)
- Создание категорий:

category1 = Category.objects.create(name="Электроника")

category2 = Category.objects.create(name="Одежда")
- Привязка магазинов к категориям:

category1.shops.add(shop1, shop2)

category2.shops.add(shop1)
- Создание продуктов:

product1 = Product.objects.create(name="Смартфон", category=category1)

product2 = Product.objects.create(name="Ноутбук", category=category1)

product3 = Product.objects.create(name="Футболка", category=category2)
- Создание информации о продуктах:

product_info1 = ProductInfo.objects.create(product=product1, shop=shop1, model="iPhone 13", external_id=1, quantity=100, price=70000, price_rrc=80000)

product_info2 = ProductInfo.objects.create(product=product2, shop=shop1, model="MacBook Pro", external_id=2, quantity=50, price=150000, price_rrc=160000)

product_info3 = ProductInfo.objects.create(product=product3, shop=shop2, model="Футболка Nike", external_id=3, quantity=200, price=1500, price_rrc=2000)
- Создание параметров:

parameter1 = Parameter.objects.create(name="Цвет")

parameter2 = Parameter.objects.create(name="Размер")
- Создание параметров продуктов:

ProductParameter.objects.create(product_info=product_info1, parameter=parameter1, value="Черный")

ProductParameter.objects.create(product_info=product_info1, parameter=parameter2, value="128 ГБ")

ProductParameter.objects.create(product_info=product_info2, parameter=parameter1, value="Серый")

ProductParameter.objects.create(product_info=product_info3, parameter=parameter1, value="Белый")

ProductParameter.objects.create(product_info=product_info3, parameter=parameter2, value="L")
- Создание контактов:

contact1 = Contact.objects.create(user=user1, city="Москва", street="Тверская", house="1", phone="123456789")

contact2 = Contact.objects.create(user=user2, city="Санкт-Петербург", street="Невский", house="2", phone="987654321")

- Создание заказов:

order1 = Order.objects.create(user=user1, state="new", contact=contact1)

order2 = Order.objects.create(user=user2, state="new", contact=contact2)

- Создание позиции заказа:

OrderItem.objects.create(order=order1, product_info=product_info1, quantity=1)

OrderItem.objects.create(order=order2, product_info=product_info3, quantity=2)

### Примечания

- Замените `ваш-логин` и `ваш_email@example.com` на свои реальные данные.
- Убедитесь, что все команды и пути соответствуют Вашему проекту.
- Вы можете дополнить документацию, добавив больше информации о функционале, примерах использования, конфигурации и т.д.
