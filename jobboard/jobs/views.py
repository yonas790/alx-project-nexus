from rest_framework import generics, status, filters, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Count, Avg
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Category, Company, JobType, Job, Application, JobView, SavedJob, JobAlert
from .serializers import (
    CategorySerializer, CompanySerializer, JobTypeSerializer,
    JobListSerializer, JobDetailSerializer, JobCreateUpdateSerializer,
    ApplicationSerializer, SavedJobSerializer, JobAlertSerializer
)


class CategoryListCreateView(generics.ListCreateAPIView):
    """List and create job categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a job category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompanyListCreateView(generics.ListCreateAPIView):
    """List and create companies"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'industry', 'location']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a company"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JobTypeListCreateView(generics.ListCreateAPIView):
    """List and create job types"""
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    ordering = ['name']


class JobTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a job type"""
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JobListView(generics.ListAPIView):
    """List all active jobs with filtering and search"""
    serializer_class = JobListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'company__name', 'location', 'tags']
    ordering_fields = ['created_at', 'title', 'salary_min', 'views_count']
    ordering = ['-created_at']
    
    def get_queryset(self):
        return Job.objects.filter(status='active').select_related(
            'company', 'category', 'job_type', 'posted_by'
        ).prefetch_related('applications')


class JobDetailView(generics.RetrieveAPIView):
    """Retrieve a specific job"""
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Track job view
        self.track_job_view(instance, request)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def track_job_view(self, job, request):
        """Track job view for analytics"""
        ip_address = self.get_client_ip(request)
        user = request.user if request.user.is_authenticated else None
        
        # Check if this view is already tracked (avoid duplicate tracking)
        existing_view = JobView.objects.filter(
            job=job,
            ip_address=ip_address,
            user=user
        ).first()
        
        if not existing_view:
            JobView.objects.create(
                job=job,
                user=user,
                ip_address=ip_address,
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
            # Update job views count
            job.views_count += 1
            job.save(update_fields=['views_count'])
    
    def get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class JobCreateView(generics.CreateAPIView):
    """Create a new job posting"""
    serializer_class = JobCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class ApplicationListCreateView(generics.ListCreateAPIView):
    """List and create job applications"""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['applied_at', 'status']
    ordering = ['-applied_at']
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Application.objects.all().select_related('job', 'applicant')
        return Application.objects.filter(applicant=self.request.user).select_related('job')


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def job_statistics(request):
    """Get job board statistics"""
    cache_key = 'job_statistics'
    stats = cache.get(cache_key)
    
    if not stats:
        stats = {
            'total_jobs': Job.objects.filter(status='active').count(),
            'total_companies': Company.objects.count(),
            'total_applications': Application.objects.count(),
            'total_categories': Category.objects.count(),
        }
        cache.set(cache_key, stats, 300)  # Cache for 5 minutes
    
    return Response(stats)
