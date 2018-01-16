from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')





































































        fields = (
            'id',
            'author',
            'title',
            'text',
            'created_date',
            'published_date',
        )

    #    read_only_fields = ('id',)
        read_only_fields = ()
