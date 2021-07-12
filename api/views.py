from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from Todo.models import todo 

# Create your views here.

class TodoView(APIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

