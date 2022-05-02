from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event, Registration
from .forms import RegistrationForm


'''
This class based view contains two querysets to sort the events
into future and past, and then display them in alphabetical order
on index.html.
'''


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


'''
This class based view displays all the information about
a particular event. The event is identified from its
unqiue pk. Then, the people who have signed up are
obtained, and for each of these registrations, the
total particpants is increased by 1, or by 2 if they
are bringing a guest. Finally, the remaining spaces
are calculated by subtracting the current number of
participants from the maximum number.
'''


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


'''
This function based view, which has a login required
decorator, enables users to register for an event. The
event is again identified by its pk, and the registration
form is loaded, and if filled in, is saved. The user is
then redirected to the page of the event that he/she had
signed up for.
'''


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


'''
This function based view, which also has a login
required decorator, enables users to unregister
for an event. It fetches the event, but also the
unique id associated with an individual
registration. It then checks to make sure that
the name corresponding to the registration matches
that of the user making the request, and deletes
it if is. The user is then redirected to the
event detail page of the event that they have just
unregistered from.
'''


@login_required
def event_unregister(request, event_id, register_id):
    event = get_object_or_404(Event, pk=event_id)
    registration = get_object_or_404(Registration, pk=register_id)
    if registration.name != request.user:
        return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
    registration.delete()
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
