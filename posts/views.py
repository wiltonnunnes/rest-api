from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from .models import Post
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	http_method_names = ['get', 'post', 'head']
	
	def list(self, request):
		queryset = self.get_queryset().exclude(owner=request.user)[:10]
		serializer = PostSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)
	http_method_names = ['post', 'head']
	
	def perform_create(self, serializer):
		serializer.save(is_active=True)