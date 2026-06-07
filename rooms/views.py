from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Room, RoomType

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'
    paginate_by = 9

    def get_queryset(self):
        queryset = Room.objects.filter(status='available')
        room_type = self.request.GET.get('type')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        capacity = self.request.GET.get('capacity')
        if room_type:
            queryset = queryset.filter(room_type__id=room_type)
        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)
        if capacity:
            queryset = queryset.filter(capacity__gte=capacity)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.all()
        return context

class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'
