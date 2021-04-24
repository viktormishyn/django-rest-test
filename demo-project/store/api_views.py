from rest_framework.generics import ListAPIView
from store.serializers import ProductSerializer
from store.models import Product

from django_filters.rest_framework import DjangoFilterBackend

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # filtering
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

    def get_queryset(self):
        # overwrite get_queryset method if 'on_sale' query parameter is set to true
        # if query parameter is false or not specified the whole queryset will be returned
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


