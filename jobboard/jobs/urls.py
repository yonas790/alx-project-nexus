from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

# Create a router for ViewSets (if any)
router = DefaultRouter()

urlpatterns = [
    # Authentication endpoints
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Category endpoints
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
    # Company endpoints
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail'),
    
    # Job Type endpoints
    path('job-types/', views.JobTypeListCreateView.as_view(), name='job-type-list'),
    path('job-types/<int:pk>/', views.JobTypeDetailView.as_view(), name='job-type-detail'),
    
    # Job endpoints
    path('jobs/', views.JobListView.as_view(), name='job-list'),
    path('jobs/create/', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/<slug:slug>/', views.JobDetailView.as_view(), name='job-detail'),
    
    # Application endpoints
    path('applications/', views.ApplicationListCreateView.as_view(), name='application-list'),
    
    # Statistics endpoint
    path('statistics/', views.job_statistics, name='job-statistics'),
]
