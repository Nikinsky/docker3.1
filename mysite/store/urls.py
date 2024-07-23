from rest_framework.urls import path
from .views import *


urlpatterns = [

    path('', UserProfileViewSet.as_view({'get': 'list', 'post':'create'}), name='userprofile_list'),
    path('int:pk', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create',}), name='category_list'),
    path('category/int:pk/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('product/', ProductViewSet.as_view({'get': 'list', 'post': 'create',}), name='product_list'),
    path('product/int:pk/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product_detail'),


    path('productphotos/', ProductPhotosViewSet.as_view({'get': 'list', 'post': 'create',}), name='productphotos_list'),
    path('productphotos/int:pk/', ProductPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='productphotos_detail'),


    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/int:pk/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='rating_detail'),


    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create',}), name='review_list'),
    path('review/int:pk/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review_detail'),


]