from django.shortcuts import render
from .serializers import user_extended_serializer, user_serializer
from rest_framework import viewsets

# Create your views here.
class user_viewsets (viewsets.ModelViewSet):
    serializer_class = user_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = user_serializer.Meta.model.objects.all()
    
class user_extended (viewsets.ModelViewSet):
    serializer_class = user_extended_serializer
    # permission_classes = (IsAuthenticated,)
    queryset = user_extended_serializer.Meta.model.objects.all()