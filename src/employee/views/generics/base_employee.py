from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from employee.permissions import IsOwnerOrReadOnlyEmployee


class BaseConfigurationEmployeeViewGeneric(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyEmployee]
