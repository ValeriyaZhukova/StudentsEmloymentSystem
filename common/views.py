from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common import serializers
from common.models import City, Industry


# Create your views here.
class CityView(APIView):
    serializer_class = serializers.CitySerializer

    def get(self, request, format=None):
        city = City.objects.all()
        serializer = self.serializer_class(city, many=True)
        return Response(serializer.data)


class CityDetailView(APIView):
    serializer_class = serializers.CitySerializer

    def get_queryset(self, pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return False
        return city

    def get(self, request, pk, format=None):
        city = self.get_queryset(pk)

        if not city:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(city)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk, format=None):
        city = self.get_queryset(pk)

        if not city:
            content = {
                "status": "Not found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        city.delete()
        return Response({"msg": "No Content"}, status=status.HTTP_204_NO_CONTENT)

    def put(self,request, pk, format=None):
        city = self.get_queryset(pk)

        if not city:
            content={
                "status":"Not Found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class IndustryView(APIView):
    serializer_class = serializers.IndustrySerializer

    def get(self, request, format=None):
        industry = Industry.objects.all()
        serializer = self.serializer_class(industry, many=True)
        return Response(serializer.data)


class IndustryDetailView(APIView):
    serializer_class = serializers.IndustrySerializer

    def get_queryset(self, pk):
        try:
            industry = Industry.objects.get(pk=pk)
        except Industry.DoesNotExist:
            return False
        return industry

    def get(self, request, pk, format=None):
        industry = self.get_queryset(pk)

        if not industry:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(industry)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk, format=None):
        industry = self.get_queryset(pk)

        if not industry:
            content = {
                "status": "Not found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        industry.delete()
        return Response({"msg": "No Content"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        industry = self.get_queryset(pk)

        if not industry:
            content = {
                "status": "Not Found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(industry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)