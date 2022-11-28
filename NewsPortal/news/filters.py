from django_filters import FilterSet
from django_filters.widgets import RangeWidget
import django_filters
from .models import Post


class PostFilter(FilterSet):
    time_of_publication = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'category': ['exact'],
        }
