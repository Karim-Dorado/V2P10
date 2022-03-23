from rest_framework.serializers import ModelSerializer
from .models import User

class UserDetailSerializer(ModelSerializer):
 
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password', 
            'is_active',
            'is_staff',
            'is_superuser',
            ]
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

class UserSerializer(ModelSerializer):
 
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            ]