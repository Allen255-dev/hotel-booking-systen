import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_booking.settings')
django.setup()

from rooms.models import Room, RoomType

# Create room types
standard, _ = RoomType.objects.get_or_create(name='Standard', defaults={'description': 'Comfortable standard room'})
deluxe, _ = RoomType.objects.get_or_create(name='Deluxe', defaults={'description': 'Spacious deluxe room with premium amenities'})
suite, _ = RoomType.objects.get_or_create(name='Suite', defaults={'description': 'Luxurious suite with panoramic views'})
penthouse, _ = RoomType.objects.get_or_create(name='Penthouse', defaults={'description': 'Exclusive penthouse with private terrace'})

# Create rooms
rooms = [
    {'room_number': '101', 'room_type': standard, 'price_per_night': 120, 'capacity': 2, 'floor': 1, 'description': 'A cozy standard room with a queen bed, modern furnishings, and city views.', 'amenities': 'WiFi, TV, Air Conditioning, Mini Bar, Safe'},
    {'room_number': '102', 'room_type': standard, 'price_per_night': 130, 'capacity': 2, 'floor': 1, 'description': 'Bright and airy standard room with garden views and premium bedding.', 'amenities': 'WiFi, TV, Air Conditioning, Balcony'},
    {'room_number': '201', 'room_type': deluxe, 'price_per_night': 220, 'capacity': 3, 'floor': 2, 'description': 'Elegant deluxe room featuring a king bed, sitting area, and stunning skyline views.', 'amenities': 'WiFi, Smart TV, Air Conditioning, Mini Bar, Bathtub, Safe, Room Service'},
    {'room_number': '202', 'room_type': deluxe, 'price_per_night': 250, 'capacity': 3, 'floor': 2, 'description': 'Spacious deluxe room with ocean views and a luxurious marble bathroom.', 'amenities': 'WiFi, Smart TV, Air Conditioning, Jacuzzi, Mini Bar, Balcony'},
    {'room_number': '301', 'room_type': suite, 'price_per_night': 450, 'capacity': 4, 'floor': 3, 'description': 'A magnificent suite with a separate living room, dining area, and breathtaking panoramic views.', 'amenities': 'WiFi, Smart TV, Air Conditioning, Jacuzzi, Full Kitchen, Butler Service, Balcony'},
    {'room_number': '302', 'room_type': suite, 'price_per_night': 500, 'capacity': 4, 'floor': 3, 'description': 'Premium corner suite flooded with natural light and featuring a private terrace.', 'amenities': 'WiFi, Smart TV, Air Conditioning, Private Terrace, Jacuzzi, Mini Bar, Safe'},
    {'room_number': '401', 'room_type': penthouse, 'price_per_night': 1200, 'capacity': 6, 'floor': 4, 'description': 'The ultimate luxury experience. A sprawling penthouse with 360-degree city views, private pool, and dedicated butler.', 'amenities': 'WiFi, Home Theater, Air Conditioning, Private Pool, Full Kitchen, Butler Service, Private Elevator, Gym'},
]

for r in rooms:
    room, created = Room.objects.get_or_create(room_number=r['room_number'], defaults=r)
    if created:
        print(f"Created room {r['room_number']}")
    else:
        print(f"Room {r['room_number']} already exists")

print("\nDone! All rooms created.")
