from django.http import JsonResponse\
    # , HttpResponse
from django.shortcuts import render

from .models import Update


# def detail_view(request):
#     # return JSON or XML data
#     # return render()
#     # render() method eventually calls HttpResponse in back
#     # return HttpResponse(get_template().render({}))  # same as render()
#     pass

def update_model_detail_view(request):
    """URL for a REST API"""
    data = {
        "title": "this is a dummy title",
        "count": 9600,
        "content": "Some dummy content"
    }
    # JsonResponse converts python dictionary into JSON dictionary
    return JsonResponse(data)
