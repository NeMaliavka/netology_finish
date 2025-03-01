from celery import shared_task
from .utils import send_invoice_email

@shared_task
def send_invoice_email_task(order_id):
    order = get_object_or_404(Order, id=order_id)
    send_invoice_email(order)