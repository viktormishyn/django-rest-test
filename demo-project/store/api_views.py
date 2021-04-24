from rest_framework.generics import ListAPIView
from store.serializers import ProductSerializer
from store.models import Product

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter

from rest_framework.pagination import LimitOffsetPagination


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
    # we can also control number of items using 'limit' query parameters

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # filtering
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')

    # pagination
    pagination_class = ProductsPagination

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
