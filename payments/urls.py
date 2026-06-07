from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('<int:booking_pk>/', views.payment_view, name='payment'),
    path('history/', views.payment_history, name='payment_history'),
]
