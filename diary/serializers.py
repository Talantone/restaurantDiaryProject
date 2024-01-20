from rest_framework import serializers
from .models import Restaurant, Visit
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


class RestaurantSerializer(serializers.ModelSerializer):
    average_evaluation = serializers.SerializerMethodField()

    def get_average_evaluation(self, obj):
        return obj.average_evaluation

    class Meta:
        model = Restaurant
        fields = ('name', 'place', 'type', 'average_evaluation')


class VisitSerializer(serializers.ModelSerializer):
    restaurant = serializers.SerializerMethodField

    class Meta:
        model = Visit
        fields = ('date_of_visit', 'expense', 'note', 'evaluation')
