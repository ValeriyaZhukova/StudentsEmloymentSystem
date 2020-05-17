from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from phone_field import PhoneField
from common.models import City, Industry
from user.models import CustomUser, Resume
from career_center.models import Institution, Faculty, CareerCenter
from company.models import Company, CompanyIndustries, StudentVacancies, Vacancy

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city')


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'industry')


class InstitutionSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Institution
        fields = ('id', 'name', 'type', 'address', 'website', 'image', 'city')


class FacultySerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    class Meta:
        model = Faculty
        fields = ('id', 'faculty', 'institution')


class CustomUserSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    role = serializers.CharField(required=True)
    avatar = serializers.FileField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'role': self.validated_data.get('role', ''),
            'avatar': self.validated_data.get('avatar', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            avatar=validated_data['avatar']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'role', 'avatar')


class CareerCenterSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    contact_person = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = CareerCenter
        fields = ('id', 'institution', 'contact_person')


class ResumeSerializer(serializers.ModelSerializer):
    student = CustomUserDetailsSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    main_industry = IndustrySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    class Meta:
        model = Resume
        fields = ('date_of_birth', 'citizenship', 'desired_position', 'working_experience', 'education_degree', 'skills',
         'resume_file', 'student', 'city', 'main_industry', 'institution')


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