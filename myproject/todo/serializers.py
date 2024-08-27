from rest_framework import serializers
from .models import Todo, Category

from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Todo serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    Todo = TodoSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

       