from rest_framework import serializers

from Backend.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    cover_img = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return str(obj.created_at.strftime('%b %d, %Y'))

    def get_cover_img(self, obj):
        return "images/"+str(obj.cover_img)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', "cover_img", 'content', 'author_name', 'author_description', 'created_at')
