from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-event_date_and_time')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):
    
    def get(self, request, id, *args, **kwargs):
        event = get_object_or_404(Event, pk=id)

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
            }
        )
