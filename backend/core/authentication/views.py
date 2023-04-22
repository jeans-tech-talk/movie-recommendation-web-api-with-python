from django.contrib.auth.models import User
from rest_framework import viewsets

from core.authentication.serializers import UserWriteSerializer, UserReadSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-id')
    write_serializer_class = UserWriteSerializer
    read_serializer_class = UserReadSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.write_serializer_class
