from rest_framework import serializers

from .models import Category, News, Job, Search


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (Category._meta.pk.name, 'name')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = (News._meta.pk.name, 'name', 'category', 'description', 'date', 'link')

class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Search
        fields = ('param', )


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('type', 'status', 'created_at', 'updated_at', 'kwargs')