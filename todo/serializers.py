from rest_framework import serializers

from todo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id', 'name', 'completed', 'user']

    user = serializers.ReadOnlyField(source='user.username')
