from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from career_center.models import Institution, CareerCenter, Faculty
from common.models import City
from common.serializers import InstitutionSerializer, FacultySerializer, CareerCenterSerializer


# Create your views here.


# Institution CRUD
class InstitutionAddView(APIView):
    permission_classes = (IsAuthenticated,)
    serializers_class = InstitutionSerializer

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            try:
                institution = Institution.objects.get(city=serializer.validated_data.get('city'))
                institution.save()
                return Response(self.serializers_class(institution).data)
            except Institution.DoesNotExist:
                serializer.save(city=City.objects.get(pk=request.data["city"]))
                return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class InstitutionGetAllView(APIView):
    serializers_class = InstitutionSerializer

    def get(self, request, format=None):
        institution = Institution.objects.all()
        serializer = self.serializers_class(institution, many=True)
        return Response(serializer.data)


class InstitutionGetView(APIView):
    serializers_class = InstitutionSerializer

    def get_queryset(self, pk):
        try:
            institution = Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            return False
        return institution

    def get(self, request, pk, format=None):
        institution = self.get_queryset(pk)

        if not institution:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(institution)
        return Response(serializer.data)


class InstitutionUpdateView(APIView):
    serializers_class = InstitutionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            institution = Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            return False
        return institution

    def put(self, request, pk, format=None):
        institution = self.get_queryset(pk)

        if not institution:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(institution, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class InstitutionDeleteView(APIView):
    serializers_class = InstitutionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            institution = Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            return False
        return institution

    def delete(self, request, pk, format=None):
        institution = self.get_queryset(pk)

        if not institution:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        institution.delete()
        return Response({'msg': 'Successfully deleted'}, status=status.HTTP_200_OK)


# Faculty CRUD
class FacultyAddView(APIView):
    permission_classes = (IsAuthenticated,)
    serializers_class = FacultySerializer

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            try:
                faculty = Faculty.objects.get(institution=serializer.validated_data.get('institution'))
                faculty.save()
                return Response(self.serializers_class(faculty).data)
            except Faculty.DoesNotExist:
                serializer.save(institution=Institution.objects.get(pk=request.data["institution"]))
                return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class FacultyGetAllView(APIView):
    serializers_class = FacultySerializer

    def get(self, request, format=None):
        faculty = Faculty.objects.all()
        serializer = self.serializers_class(faculty, many=True)
        return Response(serializer.data)


class FacultyGetView(APIView):
    serializers_class = FacultySerializer

    def get_queryset(self, pk):
        try:
            faculty = Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return False
        return faculty

    def get(self, request, pk, format=None):
        faculty = self.get_queryset(pk)

        if not faculty:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(faculty)
        return Response(serializer.data)


class FacultyUpdateView(APIView):
    serializers_class = FacultySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            faculty = Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return False
        return faculty

    def put(self, request, pk, format=None):
        faculty = self.get_queryset(pk)

        if not faculty:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(faculty, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class FacultyDeleteView(APIView):
    serializers_class = FacultySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            faculty = Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return False
        return faculty

    def delete(self, request, pk, format=None):
        faculty = self.get_queryset(pk)

        if not faculty:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        faculty.delete()
        return Response({'msg': 'Successfully deleted'}, status=status.HTTP_200_OK)


# CareerCenter CRUD
class CareerCenterAddView(APIView):
    permission_classes = (IsAuthenticated,)
    serializers_class = CareerCenterSerializer

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            try:
                career_center = CareerCenter.objects.get(contact_person=request.user,
                                                         institution=serializer.validated_data.get('institution'))
                career_center.save()
                return Response(self.serializers_class(career_center).data)
            except CareerCenter.DoesNotExist:
                serializer.save(contact_person=request.user,
                                institution=Institution.objects.get(pk=request.data["institution"]))
                return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CareerCenterGetAllView(APIView):
    serializers_class = CareerCenterSerializer

    def get(self, request, format=None):
        career_center = CareerCenter.objects.all()
        serializer = self.serializers_class(career_center, many=True)
        return Response(serializer.data)


class CareerCenterGetView(APIView):
    serializers_class = CareerCenterSerializer

    def get_queryset(self, pk):
        try:
            career_center = CareerCenter.objects.get(pk=pk)
        except CareerCenter.DoesNotExist:
            return False
        return career_center

    def get(self, request, pk, format=None):
        career_center = self.get_queryset(pk)

        if not career_center:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(career_center)
        return Response(serializer.data)


class CareerCenterUpdateView(APIView):
    serializers_class = CareerCenterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            career_center = CareerCenter.objects.get(pk=pk)
        except CareerCenter.DoesNotExist:
            return False
        return career_center

    def put(self, request, pk, format=None):
        career_center = self.get_queryset(pk)

        if not career_center:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializers_class(career_center, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CareerCenterDeleteView(APIView):
    serializers_class = CareerCenterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            career_center = CareerCenter.objects.get(pk=pk)
        except CareerCenter.DoesNotExist:
            return False
        return career_center

    def delete(self, request, pk, format=None):
        career_center = self.get_queryset(pk)

        if not career_center:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        career_center.delete()
        return Response({'msg': 'Successfully deleted'}, status=status.HTTP_200_OK)


class CareerCenterSearchView(APIView):
    serializers_class = CareerCenterSerializer

    def get(self, request, key, format=None):
        career_centers = CareerCenter.objects.filter(Q(institution__name__contains=key))
        serializer = self.serializers_class(career_centers, many=True)
        return Response(serializer.data)
