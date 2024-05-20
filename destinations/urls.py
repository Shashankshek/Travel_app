from django.urls import path
from .views import *

urlpatterns = [
    path('destinations/', DestinationListCreate.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDestroy.as_view(), name='destination-detail'),

    path('booking/',BookingListCreate.as_view(), name='booking-list'),
    path('booking/<int:pk>/', BookingRetrieveUpdateDestroy.as_view(), name='booking-detail'),
]
