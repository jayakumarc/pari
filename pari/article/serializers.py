from .models import Article, Location
from rest_framework import serializers
from rest_framework.fields import Field


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    link = Field(source='get_absolute_url')

    class Meta:
        model = Article
        fields = ('title', 'link',)


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    latLng = Field(source='get_as_latLng')
    name = Field(source='title')
    id = serializers.Field()

    class Meta:
        model = Location
        fields = ('id', 'name', 'latLng',)


class LocationArticleSerializer(serializers.HyperlinkedModelSerializer):
    articles = ArticleSerializer(source='get_articles')
    topics = ArticleSerializer(source='get_topics')
    link = Field(source='get_absolute_url')

    class Meta:
        model = Location
        fields = ('articles', 'topics', 'title', 'description', 'link',)
