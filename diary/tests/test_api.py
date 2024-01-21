from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from diary.models import Restaurant
from diary.serializers import RestaurantSerializer


class RestaurantAPITestCase(APITestCase):
    fixtures = ['restaurant.json', 'user.json']

    def test_get_restaurant_list(self):
        restaurant1 = Restaurant.objects.get(pk=2)
        restaurant2 = Restaurant.objects.get(pk=4)
        url = reverse('restaurant-list')
        response = self.client.get(url)
        serializer_data = RestaurantSerializer([restaurant1, restaurant2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_restaurant(self):
        restaurant = Restaurant.objects.get(pk=2)
        url = reverse('restaurant-detail', args=[restaurant.pk])
        response = self.client.get(url)
        serializer_data = RestaurantSerializer(restaurant).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

