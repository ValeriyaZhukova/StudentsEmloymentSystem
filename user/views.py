from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser, Resume
from common.serializers import CustomUserDetailsSerializer, ResumeSerializer
# Create your views here.


class UserRegisterView(CreateAPIView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailsSerializer
    permission_classes = (AllowAny,)


class UserGetView(APIView):
    serializers_class = CustomUserDetailsSerializer

    def get_queryset(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return False
        return user

    def get(self, request, pk, format=None):
        user = self.get_queryset(pk)

        if not user:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(user)
        return Response(serializer.data)


class ResumeAddView(APIView):
    serializers_class = ResumeSerializer

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResumeGetAllView(APIView):
    serializers_class = ResumeSerializer

    def get(self, request, format=None):
        resume = Resume.objects.all()
        serializer = self.serializers_class(resume, many=True)
        return Response(serializer.data)


class ResumeGetView(APIView):
    serializers_class = ResumeSerializer

    def get_queryset(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return False
        return user

    def get(self, request, pk, format=None):
        user = self.get_queryset(pk)

        if not user:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(user)
        return Response(serializer.data)


class ResumeGetByStudentIDView(APIView):
    serializers_class = ResumeSerializer

    def get(self, request, user_id, format=None):
        resume = Resume.objects.select_related('student').filter(student=user_id)
        serializer = self.serializers_class(resume, many=True)
        return Response(serializer.data)

