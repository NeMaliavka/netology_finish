import os
import django
from django.core.mail import send_mail
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netology_my_diplom.settings')
django.setup()

@pytest.mark.django_db
# Теперь Вы можете вызывать send_mail и другие функции Django
def test_send_email():
    result = send_mail(
        'Тестовое письмо',
        'Это тестовое письмо.',
        'ваш-логин1',
        ['ваш-логин2'],
        fail_silently=False,
    )
    assert result == 1
