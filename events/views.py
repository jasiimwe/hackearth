from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import EventDoesNotExist
from .models import Events
from .renderers import EventJSONRenderer
from .serializers import EventSerializers

# Create your views here.

class CreateEventsAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = IsAuthenticated
    renderer_classes = (EventJSONRenderer,)
    serializer_class = EventSerializers

    def post(self, request):
        event = request.data.get('event', {})
        serializer = self.serializer_class(data=event)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
