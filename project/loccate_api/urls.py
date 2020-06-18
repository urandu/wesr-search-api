from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/company/', views.CompanyListCreate.as_view()),
    path('api/v1/electrician/', views.ElectricianListCreate.as_view()),
    path('api/v1/company/<int:pk>', views.CompanyRetrieveUpdate.as_view()),
    path('api/v1/electrician/<int:pk>', views.ElectricianRetrieveUpdate.as_view()),
    path('health/', views.HealthCheck.as_view()),
]