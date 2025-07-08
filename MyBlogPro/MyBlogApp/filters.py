import django_filters
from .models import Blog, Comment


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author__username = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Blog
        fields = ['title', 'author__username', 'created_at']


class CommentFilter(django_filters.FilterSet):
    blog = django_filters.NumberFilter(field_name='blog__id')
    author__username = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Comment
        fields = ['blog', 'author__username', 'created_at']
