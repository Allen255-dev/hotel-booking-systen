from django.urls import path
from bookings import views

app_name = 'bookings'

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('create/<int:room_pk>/', views.create_booking, name='create_booking'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
