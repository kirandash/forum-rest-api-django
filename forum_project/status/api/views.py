import json
# default django view
from django.views.generic import View
from django.shortcuts import get_object_or_404
# DRF View
from rest_framework.views import APIView
from rest_framework import generics, mixins
# from rest_framework.generics import ListAPIView
# Response class to send JSON response
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer


# utility fn to check if JSON data
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


# CRUDL with one API endpoint:
# Adding Mixin to handle : List + Create
# CreateModelMixin --- post data
# UpdateModelMixin --- put data
# DestroyModelMixin --- DELETE data
class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    # using default query set with API View
    # queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    # GET call for List view
    # overwriting qs by filtering with a param q
    # search overwrite: Test: /api/status/?q=delete
    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # Overwriting GET call for detail view
    def get_object(self):
        request = self.request
        # get id from request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)  # get object
            self.check_object_permissions(request, obj)  # check permission
        return obj  # return individual object

    # overwrite DELETE method
    def perform_destroy(self, instance):
        if instance is not None:
            instance.delete()
        return None

    # overwriting default GET for List API view
    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)  # get id from request
        json_data = {}
        body_ = request.body
        if is_json(body_):  # to avoid JSONDecodeError at api endpoint
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        # request.body
        # request.data
        print(request.body)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            # retrieve will call get_object method
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # call create method of CreateModelMixin
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)  # get id from request
        json_data = {}
        body_ = request.body
        if is_json(body_):  # to avoid JSONDecodeError at api endpoint
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        # request.body
        # request.data
        print(request.body)
        requested_id = request.data.get('id', None)
        passed_id = url_passed_id or new_passed_id or requested_id or None
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)  # get id from request
        json_data = {}
        body_ = request.body
        if is_json(body_):  # to avoid JSONDecodeError at api endpoint
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        # request.body
        # request.data
        print(request.body)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)

    # http method - delete, built in method in DRF: destroy
    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)  # get id from request
        json_data = {}
        body_ = request.body
        if is_json(body_):  # to avoid JSONDecodeError at api endpoint
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        # request.body
        # request.data
        print(request.body)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)

    # overwriting the create method by not allowing user to choose which user
    # to update. And use default user
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     # Allow get method - without this: get won't be allowed
#     def get(self, request):
#         qs = Status.objects.all()  # query set must be serialized before
#         # sending into response
#         serializer = StatusSerializer(qs, many=True)
#         # return Response(qs)
#         return Response(serializer.data)
#
#     # Allow post method
#     def post(self, request):
#         qs = Status.objects.all()  # query set must be serialized before
#         # sending into response
#         serializer = StatusSerializer(qs, many=True)
#         # return Response(qs)
#         return Response(serializer.data)


# Adding Mixin to handle : List + Create
# CreateModelMixin --- post data
# UpdateModelMixin --- put data
# DestroyModelMixin --- DELETE data
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     # queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     # overwriting qs by filtering with a param q
#     # search overwrite: Test: /api/status/?q=delete
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         # call create method of CreateModelMixin
#         return self.create(request, *args, **kwargs)
#
#     # overwriting the create method by not allowing user to choose which user
#     # to update. And use default user
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# obsolete
# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     # overwriting the create method by not allowing user to choose which user
#     # to update. And use default user
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# Adding Mixin to handle : Detail + Update
# UpdateModelMixin --- put data
# class StatusDetailAPIView(
#                             # mixins.CreateModelMixin,
#                             mixins.DestroyModelMixin,
#                             mixins.UpdateModelMixin,
#                             generics.RetrieveAPIView
#                          ):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # optional if url has the default string pk mentioned
#     lookup_field = 'id'  # to map with id in url or mention pk string in url
#
#     # alternate to lookup_field with kwargs (args from url)
#     # def get_object(self):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)
#
#     def put(self, request, *args, **kwargs):
#         # call update method of UpdateModelMixin
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         # call update method of UpdateModelMixin
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         # call destroy method of DestroyModelMixin
#         return self.destroy(request, *args, **kwargs)
#
#     # It's not recommended to add create view to detail endpoint bt possible
#     # def post(self, request, *args, **kwargs):
#     #     # call create method of CreateModelMixin
#     #     return self.create(request, *args, **kwargs)


# The class below does the same thing as above but in a cleaner way
# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # optional if url has the default string pk mentioned
#     lookup_field = 'id'  # to map with id in url or mention pk string in url

# obsolete
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # lookup_field not required since pk is used in urls.py file


# obsolete
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # using default query set with API View
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'  # to map with id in url or mention pk string in url
