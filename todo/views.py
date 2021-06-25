from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo import models
from todo import serializers
from todo import permissions


class TodoViewSet(viewsets.ModelViewSet):
    """
    Todo CRUD
    """

    permission_classes = [IsAuthenticated, permissions.IsOwner]
    serializer_class = serializers.TodoSerializer

    def get_queryset(self):
        return models.Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
