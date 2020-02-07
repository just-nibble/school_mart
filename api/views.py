from django.shortcuts import render
from rest_framework import generics
from user.models import Profile
from store.models import Store
from products.models import Product
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, StoreSerializer, ProductSerializer, UserSerializer


# Create your views here.

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class StoreAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
