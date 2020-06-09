from rest_framework import serializers

from status.models import Status


class CustomSerializer(serializers.Serializer):
    # Plain Serializer
    content = serializers.CharField()
    email = serializers.EmailField()

    # Note that we don't have save() method for plain serializers, it is only
    # limited to ModelSerializer


class StatusSerializer(serializers.ModelSerializer):
    # serializing model data
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

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
