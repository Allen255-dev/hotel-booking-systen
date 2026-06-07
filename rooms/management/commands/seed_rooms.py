from django.core.management.base import BaseCommand
from rooms.models import Room, RoomType

class Command(BaseCommand):
    help = 'Seed the database with sample room data'

    def handle(self, *args, **kwargs):
        standard, _ = RoomType.objects.get_or_create(name='Standard', defaults={'description': 'Comfortable standard room'})
        deluxe, _ = RoomType.objects.get_or_create(name='Deluxe', defaults={'description': 'Spacious deluxe room'})
        suite, _ = RoomType.objects.get_or_create(name='Suite', defaults={'description': 'Luxurious suite'})
        penthouse, _ = RoomType.objects.get_or_create(name='Penthouse', defaults={'description': 'Exclusive penthouse'})

        rooms = [
            {'room_number': '101', 'room_type': standard, 'price_per_night': 120, 'capacity': 2, 'floor': 1, 'description': 'Cozy standard room with city views.', 'amenities': 'WiFi, TV, Air Conditioning, Mini Bar'},
            {'room_number': '201', 'room_type': deluxe, 'price_per_night': 220, 'capacity': 3, 'floor': 2, 'description': 'Elegant deluxe room with skyline views.', 'amenities': 'WiFi, Smart TV, Bathtub, Mini Bar'},
            {'room_number': '301', 'room_type': suite, 'price_per_night': 450, 'capacity': 4, 'floor': 3, 'description': 'Magnificent suite with panoramic views.', 'amenities': 'WiFi, Jacuzzi, Full Kitchen, Butler Service'},
            {'room_number': '401', 'room_type': penthouse, 'price_per_night': 1200, 'capacity': 6, 'floor': 4, 'description': 'Ultimate luxury penthouse with private pool.', 'amenities': 'WiFi, Private Pool, Butler Service, Gym'},
        ]

        for r in rooms:
            _, created = Room.objects.get_or_create(room_number=r['room_number'], defaults=r)
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"{status}: Room {r['room_number']}")

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
