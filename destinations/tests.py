from django.test import TestCase
from django.contrib.auth.models import User
from .models import Destination, Booking
from datetime import date

class DestinationModelTest(TestCase):

    def setUp(self):
        self.destination = Destination.objects.create(
            name="Eiffel Tower",
            country="France",
            description="A wrought-iron lattice tower on the Champ de Mars in Paris.",
            best_time_to_visit="April to June",
            category="Historical",
            image_url="http://example.com/eiffel.jpg"
        )

    def test_destination_creation(self):
        self.assertEqual(self.destination.name, "Eiffel Tower")
        self.assertEqual(self.destination.country, "France")
        self.assertEqual(self.destination.description, "A wrought-iron lattice tower on the Champ de Mars in Paris.")
        self.assertEqual(self.destination.best_time_to_visit, "April to June")
        self.assertEqual(self.destination.category, "Historical")
        self.assertEqual(self.destination.image_url, "http://example.com/eiffel.jpg")

    def test_destination_str_method(self):
        self.assertEqual(str(self.destination), "Eiffel Tower")

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.destination = Destination.objects.create(
            name="Great Wall of China",
            country="China",
            description="A series of fortifications made of stone, brick, tamped earth, wood, and other materials.",
            best_time_to_visit="September to November",
            category="Historical",
            image_url="http://example.com/greatwall.jpg"
        )
        self.booking = Booking.objects.create(
            user=self.user,
            destination=self.destination,
            travel_date=date(2024, 12, 15),
            num_of_people=4
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.destination.name, "Great Wall of China")
        self.assertEqual(self.booking.travel_date, date(2024, 12, 15))
        self.assertEqual(self.booking.num_of_people, 4)

    def test_booking_str_method(self):
        self.assertEqual(str(self.booking), f"Booking by {self.user} for {self.destination.name} on {self.booking.travel_date}")
