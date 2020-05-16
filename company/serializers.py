from rest_framework import serializers
from company.models import Company, CompanyIndustries, Vacancy
from common.serializers import CitySerializer, IndustrySerializer
from user.serializers import CustomUserDetailsSerializer


class CompanySerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    contact_person = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'website', 'image', 'city', 'contact_person')


class CompanyIndustriesSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    industry = IndustrySerializer(read_only=True)
    class Meta:
        model = CompanyIndustries
        fields = ('id', 'company', 'industry')


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'salary', 'contract_type', 'required_experience', 'duties', 'requirements', 'conditions',
        'company')


class StudentVacanciesSerializer(serializers.ModelSerializer):
    student = CustomUserDetailsSerializer(read_only=True)
    vacancy = VacancySerializer(read_only=True)
    class Meta:
        model = StudentVacancies
        fields = ('id', 'student', 'vacancy')
