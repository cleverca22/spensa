from rest_framework import serializers # This is important
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'fullName', 'address', 'phoneNumber', 'email')