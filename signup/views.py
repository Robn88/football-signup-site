from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event, Registration
from .forms import RegistrationForm


class EventList(generic.ListView):
    context_object_name = "data"
    template_name = 'index.html'
    model = Event, Registration

    def get_queryset(self, *args, **kwargs):
        now = timezone.now()
        event = Event
        context = {
            "upcoming": Event.objects.filter(event_date_and_time__gte=now)
            .order_by('event_date_and_time'),
            "past": Event.objects.filter(event_date_and_time__lte=now)
            .order_by('event_date_and_time'),
        }
        return context


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
        return HttpResponseRedirect(reverse('event_detail', args=[id]))
    form = RegistrationForm()
    template = "event_registration.html"
    context = {
        "event": event,
        "form": form,
    }
    return render(request, template, context)


@login_required
def event_unregister(request, event_id, register_id):
    event = get_object_or_404(Event, pk=event_id)
    registration = get_object_or_404(Registration, pk=register_id)
    if registration.name != request.user:
        return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
    registration.delete()
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
