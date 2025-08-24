from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'author_id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'comments_count',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['comments_count'] = instance.comments.count()
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'post_id',
            'author',
            'author_id',
            'content',
            'created_at',
            'updated_at',
        ]
