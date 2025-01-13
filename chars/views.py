from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Char
from .serializers import CharSerializer
from django.shortcuts import render
from django.http import HttpResponse


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


def chars_list(request):
    return render(request, "chars_list.html")