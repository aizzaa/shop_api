from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title']


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['slug', 'title', 'price', 'image']

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError("Price can't be below zero")
        return price


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError("Price can't be below zero")
        return price
