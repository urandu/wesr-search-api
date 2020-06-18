from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from loccate_api.models import Institution, Equipment, Company, Electrician
from loccate_api.serializers import EquipmentSerializer, ElectricianSerializer, CompanySerializer, InstitutionSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class ElectricianRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electrician.objects.all()
    serializer_class = ElectricianSerializer

class CompanyRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ElectricianListCreate(generics.ListCreateAPIView):
    queryset = Electrician.objects.all()
    serializer_class = ElectricianSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company__location','licence_class', 'listed']


class HealthCheck(APIView):
    def post(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)