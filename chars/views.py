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


#codigo comentando abaixo usa o APIView do djangoRestFramework,
#ou seja precisa implementar manualmente as rotas
"""
class CharList(APIView):
    def post(self, request):
        serializer = CharSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        chars = Char.objects.all()
        serializer = CharSerializer(chars, many=True)
        return Response(serializer.data)

class CharDetail(APIView):
    def get(self, request, pk):
        try:
            char = Char.objects.get(pk=pk)
            serializer = CharSerializer(char)
            return Response(serializer.data)
        except Char.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            char = Char.objects.get(pk=pk)
            serializer = CharSerializer(char, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Char.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            char = Char.objects.get(pk=pk)
            char.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Char.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
"""
