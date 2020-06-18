from django.contrib.auth import get_user_model
from rest_framework import serializers
# same as django reverse bt wt 1 extra dimension - can add domain name to url
from rest_framework.reverse import reverse as api_reverse

from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    # status_uri = serializers.SerializerMethodField(read_only=True)
    # recent_status_list = serializers.SerializerMethodField(read_only=True)
    statuses = serializers.HyperlinkedRelatedField(
        source='status_set',  # Status.objects.filter(user=user)
        # queryset=Status.objects.all()[:5],  # limit no of status to show
        many=True,
        read_only=True,
        lookup_field='id',
        view_name='api-status:detail',
    )
    statuses_inline = StatusInlineUserSerializer(source='status_set',
                                                 many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
            'statuses',
            'statuses_inline',
            # 'status_uri',
            # 'recent_status_list'
        ]

    def get_uri(self, obj):
        # return "/api/users/{id}/".format(id=obj.id)
        # return api_reverse("<namespace>:<view_name>",
        #                    kwargs={"username": obj.username})
        request = self.context.get('request')
        return api_reverse("api-user:detail",
                           kwargs={"username": obj.username},
                           request=request)

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
            'last': StatusInlineUserSerializer(
                qs.first(),
                context={'request': request}).data,
            # 'recent': StatusInlineUserSerializer(qs[:10], many=True).data
            'recent': StatusInlineUserSerializer(
                qs[:limit],
                context={'request': request}, many=True).data
        }
        return data

    # def get_status_uri(self, obj):
    #     return self.get_uri(obj) + "status/"

    # def get_recent_status_list(self, obj):
    #     # recent 10 status items
    #     qs = obj.status_set.all().order_by("-timestamp")[:10]  # Status.objects.filter(user=obj)
    #     return StatusInlineUserSerializer(qs, many=True).data
