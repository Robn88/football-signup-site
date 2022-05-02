from django.urls import path
from . import views


# These are all of the paths for the URLS of the application.


urlpatterns = [
    path('', views.EventList.as_view(), name='Home'),
    path('event/<int:id>', views.EventDetail.as_view(), name='event_detail'),
    path("event/registration/<int:id>", views.event_registration, name='event_registration'),
    path('event/unregister/<int:event_id>/<int:register_id>', views.event_unregister, name='event_unregister'),
]
