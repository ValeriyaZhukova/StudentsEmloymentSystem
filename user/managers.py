from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_student(self, email, password, first_name, last_name, phone_number):

        if not email:
            raise ValueError(_('The Email must be set'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role="Student",
            avatar="images/users/student-avatar.png",
        )

        user.set_password(password)
        user.save()
        return user

    def create_company_contact_person(self, email, password, first_name, last_name, phone_number):

        if not email:
            raise ValueError(_('The Email must be set'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role="Company_contact_person",
            avatar="images/users/company-avatar.png",
        )

        user.set_password(password)
        user.save()
        return user

    def create_career_center_contact_person(self, email, password, first_name, last_name, phone_number):

        if not email:
            raise ValueError(_('The Email must be set'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role="Career_center_contact_person",
            avatar="images/users/university-avatar.png",
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)