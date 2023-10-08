from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.api.serializers import PostSerializer
from blog.models import Post
from django.contrib.auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer

class PostList(generics.ListCreateAPIView):
  queryset=Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer