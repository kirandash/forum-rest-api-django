import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

# Creating a new token manually
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expires_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]

    def get_uri(self, obj):
        # return "/api/users/{id}".format(id=obj.id)
        # return "/api/users/{id}".format(id=obj.id)
        request = self.context.get('request')
        return api_reverse("api-user:detail",
                           kwargs={"username": obj.username},
                           request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
    # make password write only by overwriting
    # also add style for console
    # if password isn't write only, it will be returned in response after user
    # creation. We don't want the password hash to be visible to user
    # password = serializers.CharField(style={'input_type': 'password'},
    #                                  write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    # token_response = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            # 'token_response'
            'message'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, value):
        return "Thank you for registering. Please verify your " \
               "email before continuing"

    def validate_email(self, value):
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

    # serializer method field - get_fieldname
    def get_token(self, obj):  # instance of the model
        user = obj  # since this is user model
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expires_delta - datetime.timedelta(seconds=200)

    # alternate way to add token, expires with payload response
    # def get_token_response(self, obj):
    #     user = obj
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     context = self.context
    #     request = context['request']  # get request context from view
    #     print(request.user.is_authenticated)
    #     response = jwt_response_payload_handler(token, user,
    #                                             request=context['request'])
    #     return response

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
        # by default all users are created as active. make active false
        # later write extra fn to make it active after email verification
        user_obj.is_active = False
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
