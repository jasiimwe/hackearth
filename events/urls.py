from django.urls import path

from .views import CreateEventsAPIView

app_name = 'events'
urlpatterns = [
    path('events/', CreateEventsAPIView.as_view()),
]
