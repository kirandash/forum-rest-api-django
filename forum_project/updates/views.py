# using json library from python
import json
# Django's built in serializer
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
# to create class based view
from django.views.generic import View
from forum.mixins import JsonResponseMixin

from .models import Update


# def detail_view(request):
#     # return JSON or XML data
#     # return render()
#     # render() method eventually calls HttpResponse in back
#     # return HttpResponse(get_template().render({}))  # same as render()
#     pass

def json_dummy_view(request):
    """URL for a dummy REST API - GET method"""
    # python dictionary
    data = {
        "title": "this is a dummy title",
        "count": 9600,
        "content": "Some dummy content"
    }
    # use json library from python to convert python dictionary into JSON
    json_data = json.dumps(data)
    # HttpResponse to send json data
    return HttpResponse(json_data, content_type='application/json')
    # JsonResponse converts python dictionary into JSON dictionary
    # return JsonResponse(data)


class JsonDummyCBV(View):
    """URL for a dummy REST API - GET method"""
    def get(self, request):
        data = {
            "title": "this is CBV dummy title",
            "count": 432,
            "content": "Some CBV dummy content"
        }
        return JsonResponse(data)


class JsonDummyCBVWithMixin(JsonResponseMixin, View):
    """URL for a dummy REST API - GET method"""
    def get(self, request):
        data = {
            "title": "this is Mixin dummy title",
            "count": 12,
            "content": "Some Mixin dummy content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    """URL for a dummy REST API - GET method with serialization"""
    def get(self, request):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj], fields=('user', 'content'))
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request):
        # query set
        qs = Update.objects.all()
        # serialize: format, query string, fields to serialize
        # serialize does the same as the below mentioned fixture:
        # python manage.py dumpdata updates.update --format json --indent 4
        # data = serialize("json", qs)
        # if no fields mentioned, serializer wl return all fields
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        # no need to json dump, as we already formatted to json with serialize
        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')
