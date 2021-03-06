from rest_framework import serializers
from user.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'pk',
            'name',
            'card',
            'pin',
        ]