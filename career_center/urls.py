from career_center import views
from django.urls import path, include

urlpatterns = [
    #institution CRUD
    path('add/institution/', views.InstitutionAddView.as_view()),
    path('institution/', views.InstitutionGetAllView.as_view()),
    path('institution/<int:pk>', views.InstitutionGetView.as_view()),
    path('update/institution/<int:pk>', views.InstitutionUpdateView.as_view()),
    path('delete/institution/<int:pk>', views.InstitutionDeleteView.as_view()),
    #faculty CRUD
    path('add/faculty/', views.FacultyAddView.as_view()),
    path('faculty/', views.FacultyGetAllView.as_view()),
    path('faculty/<int:pk>', views.FacultyGetView.as_view()),
    path('update/faculty/<int:pk>', views.FacultyUpdateView.as_view()),
    path('delete/faculty/<int:pk>', views.FacultyDeleteView.as_view()),
    #career_center CRUD
    path('add/career_center/', views.CareerCenterAddView.as_view()),
    path('career_center/', views.CareerCenterGetAllView.as_view()),
    path('career_center/<int:pk>', views.CareerCenterGetView.as_view()),
    path('update/career_center/<int:pk>', views.CareerCenterUpdateView.as_view()),
    path('delete/career_center/<int:pk>', views.CareerCenterDeleteView.as_view()),
    path('search/career_center/<str:key>', views.CareerCenterSearchView.as_view())
]