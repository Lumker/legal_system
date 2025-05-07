# clients/tests.py
from django.test import TestCase
from clients.models import Client

class ClientModelTest(TestCase):
    def test_client_creation(self):
        client = Client.objects.create(
            name="John Doe",
            id_number="9001010000088",
            address="123 Main St",
            contact_info="johndoe@example.com"
        )
        saved_client = Client.objects.get(id=client.id)
        self.assertEqual(saved_client.name, "John Doe")