# documents/tests.py
from django.test import TestCase
from documents.models import Document
from cases.models import Case
from clients.models import LawFirmUser, Client  # Import both models

class DocumentModelTest(TestCase):
    def test_document_creation(self):
        # Step 1: Create a LawFirmUser (for lawyer)
        user = LawFirmUser.objects.create_user(
            username='testlawyer',
            password='testpass',
            firm_name='ABC Legal'
        )

        # Step 2: Create a Client (for the case client)
        client = Client.objects.create(
            name="John Doe",
            id_number="9001010000088",
            address="123 Main St"
        )

        # Step 3: Create a case with the Client (not LawFirmUser)
        case = Case.objects.create(
            title="Family Case",
            status="open",
            client=client,  # ✅ Use Client instance
            lawyer=user,
            court="Magistrate Court"
        )

        # Step 4: Create document linked to the case
        document = Document.objects.create(
            case=case,
            title="Affidavit",
            file="documents/affidavit.pdf"
        )

        # Step 5: Assertions
        self.assertEqual(document.title, "Affidavit")
        self.assertEqual(document.case.title, "Family Case")
        self.assertEqual(document.case.client.name, "John Doe")