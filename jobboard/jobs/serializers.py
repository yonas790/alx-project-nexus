from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category, Company, JobType, Job, Application, 
    JobView, SavedJob, JobAlert
)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""
    jobs_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'jobs_count']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_jobs_count(self, obj):
        return obj.jobs.filter(status='active').count()


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Company model"""
    jobs_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'description', 'website', 'logo', 
            'location', 'size', 'industry', 'created_at', 
            'updated_at', 'jobs_count'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_jobs_count(self, obj):
        return obj.jobs.filter(status='active').count()


class JobTypeSerializer(serializers.ModelSerializer):
    """Serializer for JobType model"""
    jobs_count = serializers.SerializerMethodField()
    
    class Meta:
        model = JobType
        fields = ['id', 'name', 'description', 'jobs_count']
    
    def get_jobs_count(self, obj):
        return obj.jobs.filter(status='active').count()


class JobListSerializer(serializers.ModelSerializer):
    """Serializer for Job model - list view"""
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    posted_by = serializers.StringRelatedField(read_only=True)
    is_expired = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company', 'category', 'job_type', 
            'location', 'is_remote', 'salary_min', 'salary_max', 
            'currency', 'experience_level', 'status', 'created_at', 
            'updated_at', 'expires_at', 'views_count', 
            'applications_count', 'is_expired', 'is_active', 'posted_by'
        ]


class JobDetailSerializer(serializers.ModelSerializer):
    """Serializer for Job model - detail view"""
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    posted_by = serializers.StringRelatedField(read_only=True)
    is_expired = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    tags_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'requirements', 'responsibilities',
            'benefits', 'company', 'category', 'job_type', 'posted_by',
            'location', 'is_remote', 'salary_min', 'salary_max', 'currency',
            'experience_level', 'status', 'created_at', 'updated_at',
            'expires_at', 'slug', 'tags', 'tags_list', 'views_count',
            'applications_count', 'is_expired', 'is_active'
        ]
        read_only_fields = ['slug', 'views_count', 'applications_count', 'created_at', 'updated_at']
    
    def get_tags_list(self, obj):
        if obj.tags:
            return [tag.strip() for tag in obj.tags.split(',')]
        return []


class JobCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating Job model"""
    
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'requirements', 'responsibilities',
            'benefits', 'company', 'category', 'job_type', 'location',
            'is_remote', 'salary_min', 'salary_max', 'currency',
            'experience_level', 'status', 'expires_at', 'tags'
        ]
    
    def validate(self, data):
        if data.get('salary_min') and data.get('salary_max'):
            if data['salary_min'] > data['salary_max']:
                raise serializers.ValidationError(
                    "Minimum salary cannot be greater than maximum salary."
                )
        return data


class ApplicationSerializer(serializers.ModelSerializer):
    """Serializer for Application model"""
    job = JobListSerializer(read_only=True)
    applicant = serializers.StringRelatedField(read_only=True)
    job_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_id', 'applicant', 'cover_letter', 'resume',
            'status', 'phone', 'email', 'linkedin_url', 'portfolio_url',
            'expected_salary', 'availability_date', 'notes', 'applied_at',
            'updated_at', 'reviewed_at'
        ]
        read_only_fields = ['applicant', 'applied_at', 'updated_at', 'reviewed_at']
    
    def create(self, validated_data):
        validated_data['applicant'] = self.context['request'].user
        return super().create(validated_data)


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating Application status (admin only)"""
    
    class Meta:
        model = Application
        fields = ['status', 'notes']
    
    def update(self, instance, validated_data):
        if 'status' in validated_data:
            instance.reviewed_at = timezone.now()
        return super().update(instance, validated_data)


class JobViewSerializer(serializers.ModelSerializer):
    """Serializer for JobView model"""
    
    class Meta:
        model = JobView
        fields = ['id', 'job', 'user', 'ip_address', 'viewed_at']
        read_only_fields = ['viewed_at']


class SavedJobSerializer(serializers.ModelSerializer):
    """Serializer for SavedJob model"""
    job = JobListSerializer(read_only=True)
    job_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = SavedJob
        fields = ['id', 'job', 'job_id', 'saved_at']
        read_only_fields = ['saved_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class JobAlertSerializer(serializers.ModelSerializer):
    """Serializer for JobAlert model"""
    categories = CategorySerializer(many=True, read_only=True)
    job_types = JobTypeSerializer(many=True, read_only=True)
    category_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True, 
        required=False
    )
    job_type_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True, 
        required=False
    )
    
    class Meta:
        model = JobAlert
        fields = [
            'id', 'name', 'keywords', 'categories', 'category_ids',
            'locations', 'job_types', 'job_type_ids', 'experience_levels',
            'salary_min', 'is_remote', 'frequency', 'is_active',
            'created_at', 'last_sent'
        ]
        read_only_fields = ['created_at', 'last_sent']
    
    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        job_type_ids = validated_data.pop('job_type_ids', [])
        validated_data['user'] = self.context['request'].user
        
        alert = super().create(validated_data)
        alert.categories.set(category_ids)
        alert.job_types.set(job_type_ids)
        return alert
    
    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids', None)
        job_type_ids = validated_data.pop('job_type_ids', None)
        
        alert = super().update(instance, validated_data)
        
        if category_ids is not None:
            alert.categories.set(category_ids)
        if job_type_ids is not None:
            alert.job_types.set(job_type_ids)
        
        return alert


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username


class JobSearchSerializer(serializers.Serializer):
    """Serializer for job search parameters"""
    query = serializers.CharField(required=False, allow_blank=True)
    category = serializers.IntegerField(required=False)
    location = serializers.CharField(required=False, allow_blank=True)
    job_type = serializers.IntegerField(required=False)
    experience_level = serializers.ChoiceField(
        choices=Job.EXPERIENCE_LEVELS, 
        required=False
    )
    is_remote = serializers.BooleanField(required=False)
    salary_min = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    salary_max = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    company = serializers.IntegerField(required=False)
    tags = serializers.CharField(required=False, allow_blank=True)
    ordering = serializers.ChoiceField(
        choices=[
            ('created_at', 'Newest First'),
            ('-created_at', 'Oldest First'),
            ('title', 'Title A-Z'),
            ('-title', 'Title Z-A'),
            ('salary_min', 'Salary Low to High'),
            ('-salary_min', 'Salary High to Low'),
        ],
        required=False,
        default='-created_at'
    )
