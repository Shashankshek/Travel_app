from django.shortcuts import render
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Destination, Booking
from .serializers import DestinationSerializer, BookingSerializer

class DestinationListCreate(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
