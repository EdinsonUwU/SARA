from ast import And
from operator import and_
from queue import Empty
from django.contrib.auth.models import User
from modulo_usuario.models import usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modulo_usuario import serializers
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import  user_serializer, usuario_serializer
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password

# Create your views here.
class user_viewsets (viewsets.ModelViewSet):
    serializer_class = user_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = user_serializer.Meta.model.objects.all()

class usuario_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = usuario_serializer.Meta.model.objects.all()