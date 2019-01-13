import coreapi

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from django.shortcuts import render_to_response
from django.views.generic import TemplateView 


class HomePageView(TemplateView):
    template_name = "home.html"


"""
class RiverViewSet(APIView):

 
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        return JsonResponse(coreapi.Client().get('https://www.yourselfquotes.com/love-shayari-in-hindi/'), safe=False)
"""
