from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import RegistrationForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-event_date_and_time')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):
    def get(self, request, id, *args, **kwargs):
        event = get_object_or_404(Event, pk=id)
        registrations = Registration.objects.filter(event=event)
        total_participants = 0
        for person in registrations:
            total_participants += 1
            if person.guest:
                total_participants += 1
        remaining_spaces = event.max_participants - total_participants
        template = "event_detail.html"
        context = {
            "event": event,
            "total_participants": total_participants,
            "registrations": registrations,
            "remaining_spaces": remaining_spaces,
        }
        return render(request, template, context)


@login_required
def event_registration(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.event = event
            form.instance.name = request.user
            form.save()
    form = RegistrationForm()
    template = "event_registration.html"
    context = {
        "event": event,
        "form": form,
    }
    return render(request, template, context)
    