from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']