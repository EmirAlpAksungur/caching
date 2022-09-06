
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics

from recipes.serializer import RecipeSerializer,RecipeDetailSerializer
from recipes.models import  Recipe

import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.core import serializers
class RecipeListCreateAPIView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, request,format=None):
        queryset = Recipe.objects.all()
        serializer  = RecipeSerializer(queryset, many = True)
        content = {
            'recipes': serializer.data
        }
        return Response(content)
       
 

class RecipeListCreateAPIViewasd(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request,format=None):
        queryset = Recipe.objects.all()
        serializer  = RecipeSerializer(queryset, many = True)
        content = {
            'recipes': serializer.data
        }
        return Response(content)


class RecipeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer  


