from django.urls import path

from diary.views import RestaurantAPIRetrieveUpdateDelete, VisitAPIListCreate, RestaurantAPIListCreate

urlpatterns = [
    path(r'restaurants/', RestaurantAPIListCreate.as_view(), name='restaurants'),
    path(r'restaurants/<int:pk>', RestaurantAPIRetrieveUpdateDelete.as_view(), name='restaurant'),
    path(r'restaurants/<int:pk>/visits/', VisitAPIListCreate.as_view(), name='visits')
]