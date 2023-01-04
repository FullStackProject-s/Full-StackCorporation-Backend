from rest_framework import generics

from employee.models import Administrator
from employee.serializers import AdministratorSerializer


class AllAdministratorsListAPIView(generics.ListAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()


class AdministratorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()


class AdministratorCreateAPIView(generics.CreateAPIView):
    serializer_class = AdministratorSerializer


class AdministratorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()


class AdministratorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
