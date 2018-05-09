from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class UserSerializer(serializers.ModelSerializer):
	#posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = User
		fields = '__all__'
		
class PostSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Post
		fields = '__all__'