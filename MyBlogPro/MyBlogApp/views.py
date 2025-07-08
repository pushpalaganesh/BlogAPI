from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from .filters import BlogFilter, CommentFilter
from .pagination import CustomPagination
from rest_framework import generics


# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomPagination
    filterset_class = BlogFilter


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    filterset_class = CommentFilter


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
