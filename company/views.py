from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common import serializers
from common.models import City, Industry
from company.models import Company, CompanyIndustries, Vacancy, StudentVacancies
# Create your views here.


class CompanyView(APIView):
    serializer_class = serializers.CompanySerializer

    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = self.serializer_class(company, many=True)
        return Response(serializer.data)


class CompanyDetailView(APIView):
    serializer_class = serializers.CompanySerializer

    def get_queryset(self, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return False
        return company

    def get(self, request, pk, format=None):
        company = self.get_queryset(pk)

        if not company:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(company)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                company = Company.objects.get(city=serializer.validated_data.get('main_industry'),
                                              contact_person=request.user)
                company.save()
                return Response(self.serializer_class(company).data)
            except Company.DoesNotExist:
                serializer.save(contact_person=request.user, city=City.objects.get(pk=request.data["city"]))
                return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk, format=None):
        company = self.get_queryset(pk)
        if not company:
            content = {
                "status": "Not found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        company.delete()
        return Response({"msg": "No Content"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        company = self.get_queryset(pk)
        if not company:
            content = {
                "status":"Not Found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CompanySearchView(APIView):
    serializers_class = serializers.CompanySerializer

    def get(self, request, key, format=None):
        companies = Company.objects.filter(Q(name__contains=key))
        serializer = self.serializers_class(companies, many=True)
        return Response(serializer.data)


class CompanyIndustriesView(APIView):
    serializer_class = serializers.CompanyIndustriesSerializer

    def get(self, request, company_id, format=None):
        company_ind = CompanyIndustries.objects.select_related('company').filter(company=company_id)
        serializer = self.serializer_class(company_ind, many=True)
        return Response(serializer.data)


class CompanyIndustriesDetailView(APIView):
    serializer_class = serializers.CompanyIndustriesSerializer

    def get(self, request, industry_id, format=None):
        company_ind = CompanyIndustries.objects.select_related('industry').filter(industry=industry_id)
        serializer = self.serializer_class(company_ind, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                company_ind = CompanyIndustries.objects.get(company=serializer.validated_data.get('company'),
                                                            industry=serializer.validated_data.get('industry'))
                company_ind.save()
                return Response(self.serializer_class(company_ind).data)
            except CompanyIndustries.DoesNotExist:
                serializer.save(company=Company.objects.get(pk=request.data["company"]),
                                industry=Industry.objects.get(pk=request.data["industry"]))
                return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VacancyView(APIView):
    serializer_class = serializers.VacancySerializer

    def get(self, request, format=None):
        vacancy = Vacancy.objects.all()
        serializer = self.serializer_class(vacancy, many=True)
        return Response(serializer.data)


class VacancyDetailView(APIView):
    serializer_class = serializers.VacancySerializer

    def get_queryset(self, pk):
        try:
            vacancy = Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            return False
        return vacancy

    def get(self, request, pk, format=None):
        vacancy = self.get_queryset(pk)

        if not vacancy:
            content = \
                {
                    'status': 'Not Found'
                }
            return Response(content, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(vacancy)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                vacancy = Vacancy.objects.get(company=serializer.validated_data.get('company'))
                vacancy.save()
                return Response(self.serializer_class(vacancy).data)
            except Vacancy.DoesNotExist:
                serializer.save(company=Company.objects.get(pk=request.data["company"]))
                return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk, format=None):
        vacancy = self.get_queryset(pk)
        if not vacancy:
            content = {
                "status": "Not found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        vacancy.delete()
        return Response({"msg": "No Content"}, status=status.HTTP_204_NO_CONTENT)

    def put(self,request, pk, format=None):
        vacancy = self.get_queryset(pk)
        if not vacancy:
            content = {
                "status":"Not Found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VacancySearchView(APIView):
    serializers_class = serializers.VacancySerializer

    def get(self, request, key, format=None):
        vacancies = Vacancy.objects.filter(Q(title__contains=key))
        serializer = self.serializers_class(vacancies, many=True)
        return Response(serializer.data)


class StudentVacanciesView(APIView):
    serializer_class = serializers.StudentVacanciesSerializer

    def get(self, request, vacancy_id, format=None):
        stud_vacancy = StudentVacancies.objects.select_related('vacancy').filter(vacancy=vacancy_id)
        serializer = self.serializer_class(stud_vacancy, many=True)
        return Response(serializer.data)


class StudentVacanciesDetailView(APIView):
    serializer_class = serializers.StudentVacanciesSerializer

    def get_queryset(self, pk):
        try:
            stud_vacancy = StudentVacancies.objects.get(pk=pk)
        except StudentVacancies.DoesNotExist:
            return False
        return stud_vacancy

    def get(self, request, student_id, format=None):
        stud_vacancy = StudentVacancies.objects.select_related('student').filter(student=student_id)
        serializer = self.serializer_class(stud_vacancy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                stud_vacancy = StudentVacancies.objects.get(student=request.user,
                                                            vacancy=serializer.validated_data.get('vacancy'))
                stud_vacancy.save()
                return Response(self.serializer_class(stud_vacancy).data)
            except StudentVacancies.DoesNotExist:
                serializer.save(student=request.user, vacancy=Vacancy.objects.get(pk=request.data["vacancy"]))
                return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk, format=None):
        stud_vacancy = self.get_queryset(pk)
        if not stud_vacancy:
            content = {
                "status": "Not found"
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        stud_vacancy.delete()
        return Response({"msg": "No Content"}, status=status.HTTP_204_NO_CONTENT)