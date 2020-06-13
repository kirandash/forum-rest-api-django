from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # make password write only by overwriting
    # also add style for console
    # if password isn't write only, it will be returned in response after user
    # creation. We don't want the password hash to be visible to user
    # password = serializers.CharField(style={'input_type': 'password'},
    #                                  write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this emailid "
                                              "already exists")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with username "
                                              "already exists")
        return value

    def validate(self, attrs):
        pw = attrs.get('password')
        pw2 = attrs.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return attrs

    # overwriting default user create method to save password
    def create(self, validated_data):
        print(validated_data)
        # user_obj = User.objects.create(
        #             username=validated_data.get('username'),
        #             email=validated_data.get('email'))
        user_obj = User(
            username=validated_data.get('username'),
            email=validated_data.get('password')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
