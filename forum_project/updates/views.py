# using json library from python
import json
# from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse
# from django.shortcuts import render

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
