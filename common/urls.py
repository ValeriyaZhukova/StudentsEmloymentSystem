from common import views
from django.urls import path, include

urlpatterns = [
    #city CRUD
    path('add/city/', views.CityDetailView.as_view()),
    path('city/', views.CityView.as_view()),
    path('city/<int:pk>', views.CityDetailView.as_view()),
    path('update/city/<int:pk>', views.CityDetailView.as_view()),
    path('delete/city/<int:pk>', views.CityDetailView.as_view()),
    #industry CRUD
    path('add/industry/', views.IndustryDetailView.as_view()),
    path('industry/', views.IndustryView.as_view()),
    path('industry/<int:pk>', views.IndustryDetailView.as_view()),
    path('update/industry/<int:pk>', views.IndustryDetailView.as_view()),
    path('delete/industry/<int:pk>', views.IndustryDetailView.as_view()),
]
