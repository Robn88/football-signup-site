from django.contrib import admin
from .models import Event


class Filter(admin.ModelAdmin):

    list_filter = ('venue', 'event_date_and_time', 'title')


admin.site.register(Event, Filter)