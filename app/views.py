from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer,GroupSerializer,CartasSerializer
from .models import Cartas
from rest_framework_api_key.permissions import HasAPIKey


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartasViewSet(viewsets.ModelViewSet):
    queryset = Cartas.objects.all()
    serializer_class = CartasSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]

