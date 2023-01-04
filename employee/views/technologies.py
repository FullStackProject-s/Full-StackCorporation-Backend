from rest_framework import generics

from employee.models import Technologies
from employee.serializers import TechnologiesSerializer


class AllTechnologiesListAPIView(generics.ListAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()


class TechnologiesRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()


class TechnologiesCreateAPIView(generics.CreateAPIView):
    serializer_class = TechnologiesSerializer


class TechnologiesDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()


class TechnologiesUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
