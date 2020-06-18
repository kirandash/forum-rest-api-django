from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from accounts.api.serializers import UserPublicSerializer
from status.models import Status


# class CustomSerializer(serializers.Serializer):
#     # Plain Serializer
#     content = serializers.CharField()
#     email = serializers.EmailField()
#
#     # Note that we don't have save() method for plain serializers, it is only
#     # limited to ModelSerializer


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user',
                                                 read_only=True)
    user_link = serializers.HyperlinkedRelatedField(
        source='user',
        lookup_field='username',
        view_name='api-user:detail',
        read_only=True
    )
    username = serializers.SlugRelatedField(
        source='user',
        read_only=True,
        slug_field='username'
    )

    # serializing model data
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'user_id',
            'user_link',
            'username',
            'content',
            'image'
        ]
        read_only_fields = ['user']  # only allowed for GET calls

    def get_uri(self, obj):
        request = self.context.get('request')
        # return "/api/status/{id}".format(id=obj.id)
        return api_reverse('api-status:detail', kwargs={"id": obj.id},
                           request=request)

    def validate_content(self, value):
        # Fn to validate content of serializer - field level validation
        if len(value) > 10000:
            raise serializers.ValidationError("This is too long")
        return value

    def validate(self, data):
        # Fn to validate all content types - model level validation
        content = data.get("content", None)  # default value None
        if content == "":  # if empty string - content set as None
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required.")
        return data


# class StatusInlineUserSerializer(serializers.ModelSerializer):
class StatusInlineUserSerializer(StatusSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # serializing model data

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]

    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     # return "/api/status/{id}".format(id=obj.id)
    #     return api_reverse('api-status:detail', kwargs={"id": obj.id},
    #                        request=request)
