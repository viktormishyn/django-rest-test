from rest_framework import serializers

from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')

    def to_representation(self, instance):
        # overwrite to_representation method in Serializer sub-class 
        # in order to order to add extra data to serialized response
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.is_on_sale()
        data['current_price'] = instance.current_price()
        return data