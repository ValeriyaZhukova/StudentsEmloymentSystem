from rest_framework import serializers
from career_center.models import Institution, Faculty, CareerCenter
from common.serializers import CitySerializer
from user.serializers import CustomUserDetailsSerializer

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


class CareerCenterSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    contact_person = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = CareerCenter
        fields = ('id', 'institution', 'contact_person')
