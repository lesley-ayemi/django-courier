from frontend.models import Shipment
import django_filters
from .models import *

class ShipmentFilter(django_filters.FilterSet):
    # ship_code = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Shipment
        fields = ['ship_code']
        # exclude = ['name']