from company import views
from django.urls import path, include

urlpatterns = [
    # company CRUD
    path('add/company/', views.CompanyDetailView.as_view()),
    path('company/', views.CompanyView.as_view()),
    path('company/<int:pk>', views.CompanyDetailView.as_view()),
    path('update/company/<int:pk>', views.CompanyDetailView.as_view()),
    path('delete/company/<int:pk>', views.CompanyDetailView.as_view()),
    path('search/company/<str:key>', views.CompanySearchView.as_view()),
    # vacancy CRUD
    path('add/vacancy/', views.VacancyDetailView.as_view()),
    path('vacancy/', views.VacancyView.as_view()),
    path('vacancy/<int:pk>', views.VacancyDetailView.as_view()),
    path('update/vacancy/<int:pk>', views.VacancyDetailView.as_view()),
    path('delete/vacancy/<int:pk>', views.VacancyDetailView.as_view()),
    path('search/vacancy/<str:key>', views.VacancySearchView.as_view()),
    # company industries CRUD
    path('add/company/industries/', views.CompanyIndustriesDetailView.as_view()),
    path('company/industries/<int:company_id>', views.CompanyIndustriesView.as_view()),
    path('industry/companies/<int:industry_id>', views.CompanyIndustriesDetailView.as_view()),
    # student vacancies CRUD
    path('add/student/vacancies/', views.StudentVacanciesDetailView.as_view()),
    path('student/vacancies/<int:student_id>', views.StudentVacanciesDetailView.as_view()),
    path('vacancy/students/<int:vacancy_id>', views.StudentVacanciesView.as_view()),
]