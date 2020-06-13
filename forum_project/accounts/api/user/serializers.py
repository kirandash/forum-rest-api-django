from django.contrib.auth import get_user_model
from rest_framework import serializers

from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    # status_uri = serializers.SerializerMethodField(read_only=True)
    # recent_status_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
            # 'status_uri',
            # 'recent_status_list'
        ]

    def get_uri(self, obj):
        return "/api/users/{id}/".format(id=obj.id)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10  # default limit
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass

        qs = obj.status_set.all().order_by("-timestamp")  # [:10]
        data = {
            'uri': self.get_uri(obj) + "status/",
            'last': StatusInlineUserSerializer(qs.first()).data,
            # 'recent': StatusInlineUserSerializer(qs[:10], many=True).data
            'recent': StatusInlineUserSerializer(qs[:limit], many=True).data
        }
        return data

    # def get_status_uri(self, obj):
    #     return self.get_uri(obj) + "status/"

    # def get_recent_status_list(self, obj):
    #     # recent 10 status items
    #     qs = obj.status_set.all().order_by("-timestamp")[:10]  # Status.objects.filter(user=obj)
    #     return StatusInlineUserSerializer(qs, many=True).data
