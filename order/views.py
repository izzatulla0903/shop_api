from urllib import request
from rest_framework import generics, permissions, response, views 
from . import serializers
from .models import Order

class CreateOrderView(generics.CreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserOrderList(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user 
        orders = user.orders.all()
        # orders = Order.objects.filter(user=user) - 2 varik
        serializer = serializers.OrderSerializer(orders, many=True).data #пишем дате если хотим вернуть сериалазер работет только в апивию
        return response.Response(serializer, status=200)

class UpdateOrderStatusView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def patch(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return response.Response('invalid status!', status=400)
        order = Order.objects.get(pk=pk)
        order.status = status 
        order.save()
        serializer = serializers.OrderSerializer(order).data 
        return response.Response(serializer, status=206)
