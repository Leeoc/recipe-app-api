# from django.contrib.auth.models import User
from rest_framework import generics

from . import serializers


class CreateUserView(generics.CreateAPIView):
    """Create new user in system"""
    serializer_class = serializers.UserSerializer
