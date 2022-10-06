from rest_framework import serializers
from users.models import User, Group


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'