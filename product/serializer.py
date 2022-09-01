from .models import Product
from rest_framework import serializers 
from django.db.models import Avg

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'image')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['raviews'] = instance.reviews.count()
        
        return repr