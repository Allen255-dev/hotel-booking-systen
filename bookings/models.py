from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booking_reference = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.booking_reference} - {self.user.username}"

    def get_num_nights(self):
        return (self.check_out_date - self.check_in_date).days

    def calculate_total(self):
        return self.room.price_per_night * self.get_num_nights()

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            import uuid
            self.booking_reference = str(uuid.uuid4()).upper()[:10]
        if not self.total_price:
            self.total_price = self.calculate_total()
        super().save(*args, **kwargs)

class BookingHistory(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='history')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    note = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.booking_reference}: {self.old_status} → {self.new_status}"
