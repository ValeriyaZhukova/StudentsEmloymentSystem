from rest_auth.registration.serializers import RegisterSerializer
from user.models import CustomUser, Resume
from common.serializers import CitySerializer, IndustrySerializer
from career_center import InstitutionSerializer

class CustomUserSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.PhoneField(required=False)
    role = serializers.CharField(required=True)
    avatar = serializers.FileField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'role': self.validated_data.get('role', ''),
            'avatar': self.validated_data.get('avatar', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'role', 'avatar')
        read_only_fields = ('email',)


class ResumeSerializer(serializers.ModelSerializer):
    student = CustomUserDetailsSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    main_industry = IndustrySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    class Meta:
        model = Resume
        fields = ('id', 'date_of_birth', 'citizenship', 'desired_position', 'working_experience', 'education_degree', 'skills',
         'resume_file', 'student', 'city', 'main_industry', 'institution')