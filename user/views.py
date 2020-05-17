from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser, Resume
from common.serializers import CustomUserDetailsSerializer, ResumeSerializer
# Create your views here.


#User CRUD
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


class UserUpdateView(APIView):
    serializers_class = CustomUserDetailsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def get_queryset(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return False
        return user

    def put(self, request, pk, format=None):
        user = self.get_queryset(pk)

        if not user:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#Resume CRUD
class ResumeAddView(APIView):
    permission_classes = (IsAuthenticated,)
    serializers_class = ResumeSerializer

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
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
            resume = Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            return False
        return resume

    def get(self, request, pk, format=None):
        resume = self.get_queryset(pk)

        if not resume:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(resume)
        return Response(serializer.data)


class ResumeUpdateView(APIView):
    serializers_class = ResumeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            resume = Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            return False
        return resume

    def put(self, request, pk, format=None):
        recipe = self.get_queryset(pk)

        if not recipe:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResumeDeleteView(APIView):

    def delete(self, request, pk, format=None):
        resume = self.get_queryset(pk)

        if not resume:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        resume.delete()
        return Response({'msg': 'Successfully deleted'}, status=status.HTTP_200_OK)

