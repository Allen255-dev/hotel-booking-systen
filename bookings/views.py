from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View
from .models import Booking
from rooms.models import Room
from datetime import date

@method_decorator(login_required, name='dispatch')
class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')

@method_decorator(login_required, name='dispatch')
class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'

@login_required
def create_booking(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if request.method == 'POST':
        check_in = request.POST.get('check_in_date')
        check_out = request.POST.get('check_out_date')
        num_guests = request.POST.get('num_guests', 1)
        special_requests = request.POST.get('special_requests', '')
        if check_in and check_out:
            booking = Booking.objects.create(
                user=request.user,
                room=room,
                check_in_date=check_in,
                check_out_date=check_out,
                num_guests=num_guests,
                special_requests=special_requests,
            )
            messages.success(request, f'Booking {booking.booking_reference} created successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    return render(request, 'bookings/create_booking.html', {'room': room, 'today': date.today()})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status in ['pending', 'confirmed']:
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    return redirect('bookings:booking_list')
