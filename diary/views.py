from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Restaurant, Visit
from .permissions import IsRestaurantOwner, IsOwnerOrReadOnly
from .serializers import RestaurantSerializer, VisitSerializer
from .generics import UpdateDestroyAPIView


class RestaurantAPIListCreate(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        # when a restaurant is saved, its saved how it is the owner
        serializer.save(user=self.request.user)


class RestaurantAPIRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class VisitAPIListCreate(generics.ListCreateAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
    permission_classes = (IsRestaurantOwner,)

    def perform_create(self, serializer):
        # saves visit with restaurant_id from URL
        serializer.save(restaurant_id=self.kwargs['pk'])
