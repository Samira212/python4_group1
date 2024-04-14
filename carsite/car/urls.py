from django.urls import path
from .views import *


urlpatterns = [
    path('', CarViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='car_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('marka/', MarkaViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='car_list'),
    path('marka/<int:pk>/', MarkaViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('model/', ModelViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='car_list'),
    path('model/<int:pk>/', ModelViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('bet/', BetViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='bet_list'),
    path('bet/<int:pk>/', BetViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='bet_detail'),

    path('carphoto/', CarPhotoViewSets.as_view({'get': 'list',
                                  'post': 'create'}), name='carphoto_list'),
    path('carphoto/<int:pk>/', CarPhotoViewSets.as_view({'get': 'retrieve',
                                           'put': 'update', 'delete': 'destroy'}),
         name='carphoto_detail')
]