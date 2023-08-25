from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from todo.models import ToDo
from todo.serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
