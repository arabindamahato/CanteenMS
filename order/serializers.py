from rest_framework import serializers
from order.models import Order, OrderItem




class OrderListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order_detail', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'timestamp', 'item', 'active', 'price', 'url']


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'timestamp', 'item', 'active', 'price', 'url']


class OrderItemListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order_item_detail', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'price', 'url',]


class OrderItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'price', 'url',]