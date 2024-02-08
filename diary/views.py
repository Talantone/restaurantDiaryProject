from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant, Visit
from .permissions import IsRestaurantOwner, IsOwner
from .serializers import RestaurantSerializer, VisitSerializer
from django.core.exceptions import ObjectDoesNotExist
from .generics import UpdateDestroyAPIView


class RestaurantAPICreate(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # when a restaurant is saved, its saved how it is the owner
        serializer.save(user=self.request.user)


class RestaurantAPIList(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset


class RestaurantAPIRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsOwner,)


class VisitAPIListCreate(generics.ListCreateAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, IsRestaurantOwner,)

    def get_queryset(self):
        try:
            restaurant = Restaurant.objects.get(id=self.kwargs['pk'], user=self.request.user.id)
            return self.queryset.filter(restaurant=restaurant.id)
        except ObjectDoesNotExist:
            return []

    def perform_create(self, serializer):
        # saves visit with restaurant_id from URL
        serializer.save(restaurant_id=self.kwargs['pk'])
