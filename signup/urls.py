from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='Home'),
    path('event/<int:id>', views.EventDetail.as_view(), name='event_detail'),
    path("event/registration/<int:id>", views.event_registration, name='event_registration'),
]
