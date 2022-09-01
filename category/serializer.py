
from .models import Category
from rest_framework import serializers
from rest_framework import generics
from product.serializer import ProductListSerializer

class CategoryListCategory(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
     representation = super().to_representation(instance)
     representation['products'] = ProductListSerializer(instance.products.all(), many=True).data
     return representation