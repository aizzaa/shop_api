from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = ['author', 'body', 'product']

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = self.Meta.model.objects.create(**validated_data, author=user)
        return comment
