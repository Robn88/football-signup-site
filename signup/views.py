from django.shortcuts import render
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-event_date_and_time')
    template_name = 'index.html'
    paginate_by = 6
