from rest_framework import serializers
from products.models import Product
from django.contrib.auth.models import User
from store.models import Store
from user.models import Profile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'catalogue')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('username')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        models = Store
        fields = ('name', 'location', 'category', 'phone_number')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = Profile
        fields = (
            'user', 'first_name', 'last_name', 'email', 'store', 'school')
