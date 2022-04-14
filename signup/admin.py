from django.contrib import admin
from .models import Event, Registration


class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'event_date_and_time', 'venue')
    list_filter = ('venue', 'event_date_and_time', 'title')
    search_fields = ('venue', 'event_date_and_time', 'created_by')


class RegistrationAdmin(admin.ModelAdmin):

    list_display = ('name', 'event', 'ball', 'bibs', 'guest')


admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
