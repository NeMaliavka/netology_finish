from django.core.mail import send_mail
from django.conf import settings


def send_invoice_email(order):
    """
    Отправляет накладную на email администратора.
    :param order: Заказ, для которого отправляется накладная
    """

    subject = f"Накладная для заказа #{order.id}"
    message = f"Здравствуйте,\n\nВаш заказ #{order.id} был исполнен.\n\nДетали заказа:\n"

    for item in order.ordered_items.all():
        message += f"Продукт: {item.product_info.product.name}, Количество: {item.quantity}, Магазин: {item.product_info.shop.name}\n"

    message += "\nСпасибо за Ваш заказ!"
    recipient_list = ['ваш-логин2']  # Укажите email администратора

    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
