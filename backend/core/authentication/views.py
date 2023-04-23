from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.serializers import UserWriteSerializer, UserReadSerializer, MeSerializer, \
    ChangePasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-id')
    write_serializer_class = UserWriteSerializer
    read_serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return self.write_serializer_class
        return self.serializer_class

    @action(detail=False, serializer_class=MeSerializer)
    def me(self, request):
        self.kwargs['pk'] = request.user.pk
        return super().retrieve(request)

    @action(methods=['put'], detail=True, url_path='change-password', serializer_class=ChangePasswordSerializer)
    def change_password(self, request, pk=None):
        super().update(request)
        return Response({'detail': 'Change password successful'})
