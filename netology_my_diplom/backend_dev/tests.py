from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Order

class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.order = Order.objects.create(user=self.user, state='new')

    def test_fulfill_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.patch(url, {'state': 'confirmed'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.state, 'confirmed')