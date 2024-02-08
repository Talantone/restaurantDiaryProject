from django.contrib.auth.models import User
from django.test import TestCase

from diary.models import Restaurant, Visit
from diary.serializers import RestaurantSerializer, VisitSerializer


class RestaurantSerializerTestCase(TestCase):
    fixtures = ['user.json']

    def test_ok(self):
        restaurant = Restaurant.objects.create(user=User.objects.get(pk=4), name='pivo', place='Prague', type='pivo')
        data = RestaurantSerializer(restaurant).data
        expected_data = {
            'name': 'pivo',
            'place': 'Prague',
            'type': 'pivo',
            'average_evaluation': {'evaluation__avg': None},
            'total_spending': {'expense__sum': None}
        }

        self.assertEqual(expected_data, data)


class VisitSerializerTestCase(TestCase):
    fixtures = ['user.json', 'restaurant.json']

    def test_ok(self):
        visit = Visit.objects.create(restaurant=Restaurant.objects.get(pk=4), date_of_visit='2024-01-18', expense=1200,
                                     note="Best pivo in Prague", evaluation=5)
        data = VisitSerializer(visit).data
        expected_data = {
            "date_of_visit": "2024-01-18",
            "expense": 1200,
            "note": "Best pivo in Prague",
            "evaluation": 5
        }
        self.assertEqual(expected_data, data)
