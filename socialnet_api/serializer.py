from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=7, write_only=True, required=True)
    password2 = serializers.CharField(min_length=7, write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate_first_name(self, value):
        return value.capitalize()

    def validate_last_name(self, value):
        return value.capitalize()

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError("Password didn't match!")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'author', 'created_at', 'text', 'likes', 'dislikes')

    def to_representation(self, instance):
        representation = super().to_representation(
            instance)
        representation['images'] = PostImageSerializer(
            instance.images.all(),
            many=True,
            context=self.context).data
        return representation


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'
