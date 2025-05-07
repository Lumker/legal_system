from django.test import TestCase
from cases.models import Case
from clients.models import LawFirmUser, Client

class CaseModelTest(TestCase):
    def test_case_creation(self):
        # Create firm user (lawyer)
        user = LawFirmUser.objects.create_user(
            username='testlawyer',
            password='testpass',
            firm_name='ABC Legal'
        )

        # Create external client
        client = Client.objects.create(
            name="John Doe",
            id_number="9001010000088",
            address="123 Main St"
        )

        # Create case with client and lawyer
        case = Case.objects.create(
            title="Family Case",
            status="open",
            client=client,
            lawyer=user,
            court="Magistrate Court"
        )

        # Test assertions
        self.assertEqual(case.status, "open")
        self.assertEqual(case.client.name, "John Doe")
        self.assertEqual(case.lawyer.firm_name, "ABC Legal")