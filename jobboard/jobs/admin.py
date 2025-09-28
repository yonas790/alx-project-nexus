from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Category, Company, JobType, Job, Application, 
    JobView, SavedJob, JobAlert
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry', 'location', 'size', 'created_at']
    search_fields = ['name', 'industry', 'location']
    list_filter = ['industry', 'size', 'created_at']
    ordering = ['name']


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'company', 'category', 'location', 'status', 
        'experience_level', 'created_at', 'views_count', 'applications_count'
    ]
    list_filter = [
        'status', 'experience_level', 'is_remote', 'category', 
        'job_type', 'company', 'created_at'
    ]
    search_fields = ['title', 'description', 'company__name', 'location']
    readonly_fields = ['views_count', 'applications_count', 'created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'requirements', 'responsibilities', 'benefits')
        }),
        ('Company & Category', {
            'fields': ('company', 'category', 'job_type', 'posted_by')
        }),
        ('Location & Salary', {
            'fields': ('location', 'is_remote', 'salary_min', 'salary_max', 'currency')
        }),
        ('Job Details', {
            'fields': ('experience_level', 'status', 'expires_at')
        }),
        ('SEO & Analytics', {
            'fields': ('slug', 'tags', 'views_count', 'applications_count')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'applicant', 'job', 'status', 'applied_at', 'phone', 'email'
    ]
    list_filter = ['status', 'applied_at', 'job__company', 'job__category']
    search_fields = [
        'applicant__username', 'applicant__email', 'job__title', 
        'job__company__name', 'phone', 'email'
    ]
    readonly_fields = ['applied_at', 'updated_at']
    ordering = ['-applied_at']
    
    fieldsets = (
        ('Application Details', {
            'fields': ('job', 'applicant', 'cover_letter', 'resume', 'status')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'linkedin_url', 'portfolio_url')
        }),
        ('Additional Information', {
            'fields': ('expected_salary', 'availability_date', 'notes')
        }),
        ('Timestamps', {
            'fields': ('applied_at', 'updated_at', 'reviewed_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(JobView)
class JobViewAdmin(admin.ModelAdmin):
    list_display = ['job', 'user', 'ip_address', 'viewed_at']
    list_filter = ['viewed_at', 'job__company', 'job__category']
    search_fields = ['job__title', 'user__username', 'ip_address']
    readonly_fields = ['viewed_at']
    ordering = ['-viewed_at']


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'saved_at']
    list_filter = ['saved_at', 'job__company', 'job__category']
    search_fields = ['user__username', 'job__title', 'job__company__name']
    ordering = ['-saved_at']


@admin.register(JobAlert)
class JobAlertAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'user', 'frequency', 'is_active', 'created_at', 'last_sent'
    ]
    list_filter = ['frequency', 'is_active', 'created_at', 'is_remote']
    search_fields = ['name', 'user__username', 'keywords', 'locations']
    filter_horizontal = ['categories', 'job_types']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Alert Details', {
            'fields': ('user', 'name', 'frequency', 'is_active')
        }),
        ('Search Criteria', {
            'fields': ('keywords', 'categories', 'locations', 'job_types', 'experience_levels')
        }),
        ('Salary & Remote', {
            'fields': ('salary_min', 'is_remote')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_sent'),
            'classes': ('collapse',)
        }),
    )
