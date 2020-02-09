from django.urls import path

from .views import UserAPIView, ProductAPIView, StoreAPIView, ProfileAPIView, DetailProductAPIView, DetailProfileAPIView, DetailStoreAPIView, DetailUserAPIView

urlpatterns = [
    path('users/<int:pk>/', DetailUserAPIView.as_view()),
    path('users/', UserAPIView.as_view(), name='user_create'),
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', DetailProductAPIView.as_view()),
    path('store/', StoreAPIView.as_view()),
    path('store/<int:pk>/', DetailStoreAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    path('profile/<int:pk>/', DetailStoreAPIView.as_view()),
]
