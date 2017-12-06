from django.shortcuts import render
from django.db.models import Q
from .models import Clock
from .serializers import ClockSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from .filters import OwnerFilterBackend
# Create your views here.


class ClockList (generics.ListAPIView):

    queryset = Clock.objects.all()
    serializer_class = ClockSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or (IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, OwnerFilterBackend)
    filter_fields = '__all__'

class ClockDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Clock.objects.all()
    serializer_class = ClockSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or (IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, OwnerFilterBackend)
    filter_fields = '__all__'