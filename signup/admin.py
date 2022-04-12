from django.contrib import admin
from .models import Event


class Filter(admin.ModelAdmin):

    list_display = ('title', 'event_date_and_time', 'venue')
    list_filter = ('venue', 'event_date_and_time', 'title')
    search_fields = ('venue', 'event_date_and_time', 'created_by')


admin.site.register(Event, Filter)