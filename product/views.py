from multiprocessing import context
from django.shortcuts import render
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from . import serializer
from .models import Product
from rest_framework.decorators import action



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializer.ProductListSerializer
        return serializer.ProductDetailSerializer

    #api/v1/products/<id>/reviews/  
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data 
            return response.Response(serializer, status=200)
        data = request.data 
        serializer = ReviewSerializer(data=data, context={'request': request, 'product': product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)


    
        
