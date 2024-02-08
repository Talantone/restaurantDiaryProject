# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
#
# from diary.models import Restaurant
# from diary.serializers import RestaurantSerializer
#
#
# class RestaurantAPITestCase(APITestCase):
#     fixtures = ['restaurant.json', 'user.json']
#
#     def test_get_restaurant_list(self):
#         restaurant1 = Restaurant.objects.get(pk=2)
#         user = User.objects.get(pk=5)
#         self.client.force_login(user)
#         url = reverse('restaurant-list')
#         response = self.client.get(url)
#         serializer_data = RestaurantSerializer(restaurant1).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)
#
#     def test_get_restaurant_when_user_is_not_owner(self):
#         user = User.objects.create(username='some', email='some@email.com', password='password')
#         user.is_active = True
#         user.save()
#         auth_url = reverse('token_obtain_pair')
#         auth_response = self.client.post(auth_url, {'username': 'some',
#                                                     'password': 'password'},
#                                          format='json')
#         self.assertEqual(auth_response, status.HTTP_200_OK)
#         print(auth_response.data)
#         client = APIClient()
#         client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
#         restaurant = Restaurant.objects.get(pk=2)
#         url = reverse('restaurant-detail', args=[restaurant.pk])
#         response = client.get(url)
#         serializer_data = RestaurantSerializer(restaurant).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)
#
