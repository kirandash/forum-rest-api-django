# default django view
from django.views.generic import View
# DRF View
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework.generics import ListAPIView
# Response class to send JSON response
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    # Allow get method - without this: get won't be allowed
    def get(self, request):
        qs = Status.objects.all()  # query set must be serialized before
        # sending into response
        serializer = StatusSerializer(qs, many=True)
        # return Response(qs)
        return Response(serializer.data)

    # Allow post method
    def post(self):
        qs = Status.objects.all()  # query set must be serialized before
        # sending into response
        serializer = StatusSerializer(qs, many=True)
        # return Response(qs)
        return Response(serializer.data)


class StatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    # using default query set with API View
    # queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # overwriting qs by filtering with a param q
    # search overwrite: Test: /api/status/?q=delete
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    # using default query set with API View
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # overwriting the create method by not allowing user to choose which user
    # to update. And use default user
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    # using default query set with API View
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # optional if url has the default string pk mentioned
    lookup_field = 'id'  # to map with id in url or mention pk string in url

    # alternate to lookup_field with kwargs (args from url)
    # def get_object(self):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)
