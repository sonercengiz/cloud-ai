from rest_framework import serializers

class UserIdSerializer(serializers.Serializer):
    userId = serializers.IntegerField(read_only=True)