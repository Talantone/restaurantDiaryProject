from django.urls import path

from diary.views import RestaurantAPIRetrieveUpdateDelete, VisitAPIListCreate, RestaurantAPICreate, \
    RestaurantAPIList

urlpatterns = [
    path(r'restaurants/', RestaurantAPIList.as_view(), name='restaurant-list'),
    path(r'restaurants/', RestaurantAPICreate.as_view(), name='restaurant-create'),
    path(r'restaurants/<int:pk>', RestaurantAPIRetrieveUpdateDelete.as_view(), name='restaurant-detail'),
    path(r'restaurants/<int:pk>/visits/', VisitAPIListCreate.as_view(), name='visit-list')
]