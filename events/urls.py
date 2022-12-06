from django.urls import path

from .views import CreateEventsAPIView, all_events, get_events_view, update_event, delete_event, get_events_organization

app_name = 'events'
urlpatterns = [
    path('events/', CreateEventsAPIView.as_view()),
    path('get_event/<str:event_name>/', get_events_view),
    path('all_events/', all_events),
    path('update_event/<pk>/', update_event),
    path('delete_event/<pk>/', delete_event),
    path('get_events_organization/<int:organization_id>/', get_events_organization)
]
