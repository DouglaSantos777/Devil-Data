from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Char
from .serializers import CharSerializer


class CharListCreate(generics.ListCreateAPIView):
  queryset = Char.objects.all()
  serializer_class = CharSerializer

  def delete(self, request, *args, **kwargs):
    Char.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class CharRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
   queryset = Char.objects.all()
   serializer_class = CharSerializer
   lookup_field = "pk"