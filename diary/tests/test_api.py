from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from diary.models import Restaurant
from diary.serializers import RestaurantSerializer


class RestaurantAPITestCase(APITestCase):
    fixtures = ['restaurant.json', 'user.json']

    def test_get_restaurant_list_when_user_is_not_authenticated(self):

        url = reverse('restaurant-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_restaurant_list(self):
        restaurant1 = Restaurant.objects.get(pk=2)
        user = User.objects.get(pk=5)
        self.client.force_authenticate(user)
        url = reverse('restaurant-list')
        response = self.client.get(url)
        serializer_data = RestaurantSerializer([restaurant1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_restaurant_when_user_is_not_owner(self):
        user = User.objects.get(pk=4)
        self.client.force_authenticate(user)
        restaurant = Restaurant.objects.get(pk=2)
        url = reverse('restaurant-detail', args=[restaurant.pk])
        response = self.client.get(url)

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_get_restaurant_when_user_is_owner(self):
        user = User.objects.get(pk=5)
        self.client.force_authenticate(user)
        restaurant = Restaurant.objects.get(pk=2)
        url = reverse('restaurant-detail', args=[restaurant.pk])
        response = self.client.get(url)
        serializer_data = RestaurantSerializer(restaurant).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
