from django.urls import path

from .views import UserAPIView, ProductAPIView, StoreAPIView, ProfileAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('store/', StoreAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]
