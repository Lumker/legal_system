# deadlines/tests.py
from django.test import TestCase
from deadlines.models import Deadline
from cases.models import Case
from clients.models import LawFirmUser, Client

class DeadlineModelTest(TestCase):
    def test_deadline_creation(self):
        # Create lawyer (LawFirmUser)
        user = LawFirmUser.objects.create_user(
            username='testlawyer',
            password='testpass',
            firm_name='ABC Legal'
        )
        # Create client
        client = Client.objects.create(
            name="John Doe",
            id_number="9001010000088",
            address="123 Main St"
        )
        # Create case
        case = Case.objects.create(
            title="Family Case",
            status="open",
            client=client,
            lawyer=user,
            court="Magistrate Court"
        )
        # Create deadline
        deadline = Deadline.objects.create(
            case=case,
            description="Final filing",
            date="2024-12-31"
        )
        self.assertEqual(deadline.description, "Final filing")
        self.assertEqual(deadline.notified, False)