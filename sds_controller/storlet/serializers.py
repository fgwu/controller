from django.forms import widgets
from rest_framework import serializers
from storlet.models import Storlet


# class StorletSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=False, max_length=100)
#     path = serializers.CharField(required=False, allow_blank=False, max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Storlet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('name', instance.name)
#         instance.code = validated_data.get('path', instance.path)
#         instance.save()
#         return instance
class StorletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storlet
        fields = ('id', 'name', 'path', 'deployed', 'lenguage',
                  'interface_version', 'object_metadata', 'main',
                  'dependency', 'created_at')

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ('name', 'deployed', 'version', 'path', 'permissions', 'created_at')