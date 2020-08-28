from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email',"first_name","last_name","password","username","phone_number")
    
    def create(self, validated_data):
        print("************************")
        print(validated_data['password'])
        print([temp for temp in validated_data.keys()])
        user = MyUser.objects.create_user(**validated_data)
        return user

# create a serializer to view
# create a serializer to signup 
# the sign up serializer must contain the passwor field
# the vview users doesnnt have to contain the password field


class MyUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email',"first_name","last_name","phone_number","username")