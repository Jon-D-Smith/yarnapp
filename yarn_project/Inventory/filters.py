import django_filters

from django_filters import CharFilter

from .models import *



class YarnFilter(django_filters.FilterSet):
    color = CharFilter(field_name='color', label="Color", lookup_expr='icontains')
    brand = CharFilter(field_name='brand', label="Brand", lookup_expr='icontains')

    class Meta:
        model = Yarn
        fields = ['color', 'brand', 'weight', 'color_group']
        