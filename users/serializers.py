from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    is_valid_email = serializers.SerializerMethodField(read_only=True)
    is_valid_phone = serializers.SerializerMethodField(read_only=True)
    hobbies = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "hobbies",
            "is_valid_email",
            "is_valid_phone",
        ]

    def get_is_valid_email(self, obj):
        if obj.email_validated_at:
            return True
        return False
    
    def get_is_valid_phone(self, obj):
        if obj.phone_validated_at:
            return True
        return False


class UserRegisterSerializer(serializers.ModelSerializer):
    hobbies = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "hobbies",
        ]

    def create(self, data):
        user_obj = User.objects.create_user(
            username=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data["phone"],
            hobbies=data["hobbies"],
        )
        user_obj.save()
        return user_obj
