from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.views import views


def hello_world(request):
    return HttpResponse('Hello World')


# class my_views(views):
#     def get(self, request):
#         return HttpResponse('Hello World')

#     def post(self, request):
#         return HttpResponse('Hello World')
