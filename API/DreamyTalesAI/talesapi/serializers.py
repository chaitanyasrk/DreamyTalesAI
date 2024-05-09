from rest_framework import serializers


class StorySerializer(serializers.Serializer):
    kid_name = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    hobbies = serializers.ListField(child=serializers.CharField(max_length=100))
