from user import views
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    #user login/CRUD
    path('admin/', admin.site.urls),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserRegisterView.as_view()),
    path('user/<int:pk>', views.UserGetView.as_view()),
    path('update/user/<int:pk>', views.UserUpdateView.as_view()),
    #resume CRUD
    path('add/resume/', views.ResumeAddView.as_view()),
    path('resume/', views.ResumeGetAllView.as_view()),
    path('resume/<int:pk>', views.ResumeGetView.as_view()),
    path('update/resume/<int:pk>', views.ResumeUpdateView.as_view()),
    path('delete/resume/<int:pk>', views.ResumeDeleteView.as_view()),

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
