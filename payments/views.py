from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Payment
from bookings.models import Booking
import os

@login_required
def payment_view(request, booking_pk):
    booking = get_object_or_404(Booking, pk=booking_pk, user=request.user)
    if request.method == 'POST':
        payment, created = Payment.objects.get_or_create(
            booking=booking,
            user=request.user,
            defaults={'amount': booking.total_price, 'method': 'card'}
        )
        payment.status = 'completed'
        payment.paid_at = timezone.now()
        payment.save()
        booking.status = 'confirmed'
        booking.save()
        messages.success(request, 'Payment successful! Your booking is confirmed.')
        return redirect('bookings:booking_detail', pk=booking.pk)
    return render(request, 'payments/payment.html', {
        'booking': booking,
        'stripe_public_key': os.getenv('STRIPE_PUBLIC_KEY'),
    })

@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'payments/payment_history.html', {'payments': payments})
