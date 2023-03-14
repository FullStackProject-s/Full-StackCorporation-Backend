import django_filters as filters
from user.models import CustomUser


class CustomUserFilter(filters.FilterSet):
    id = filters.NumberFilter()
    id__gt = filters.NumberFilter(
        field_name='id',
        lookup_expr='gt'
    )
    id__lt = filters.NumberFilter(
        field_name='id',
        lookup_expr='lt'
    )

    username = filters.CharFilter(lookup_expr='icontains')
    ordering = filters.OrderingFilter(

        fields=(
            ('username', 'username'),
        )
    )
    staff_role__role_name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = CustomUser
        fields = ['id', 'username']
