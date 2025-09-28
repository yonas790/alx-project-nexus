import django_filters
from django.db.models import Q
from .models import Job


class JobFilter(django_filters.FilterSet):
    """Filter for job listings"""
    
    # Text search
    search = django_filters.CharFilter(method='filter_search')
    
    # Category and company filters
    category = django_filters.NumberFilter(field_name='category__id')
    company = django_filters.NumberFilter(field_name='company__id')
    job_type = django_filters.NumberFilter(field_name='job_type__id')
    
    # Location filters
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    is_remote = django_filters.BooleanFilter(field_name='is_remote')
    
    # Experience level filter
    experience_level = django_filters.ChoiceFilter(choices=Job.EXPERIENCE_LEVELS)
    
    # Salary filters
    salary_min = django_filters.NumberFilter(field_name='salary_min', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary_max', lookup_expr='lte')
    
    # Date filters
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    
    # Tags filter
    tags = django_filters.CharFilter(method='filter_tags')
    
    class Meta:
        model = Job
        fields = ['search', 'category', 'company', 'job_type', 'location', 
                 'is_remote', 'experience_level', 'salary_min', 'salary_max',
                 'created_after', 'created_before', 'tags']
    
    def filter_search(self, queryset, name, value):
        """Search across multiple fields"""
        if not value:
            return queryset
        
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(company__name__icontains=value) |
            Q(location__icontains=value) |
            Q(tags__icontains=value)
        )
    
    def filter_tags(self, queryset, name, value):
        """Filter by tags (comma-separated)"""
        if not value:
            return queryset
        
        tags = [tag.strip() for tag in value.split(',') if tag.strip()]
        if not tags:
            return queryset
        
        query = Q()
        for tag in tags:
            query |= Q(tags__icontains=tag)
        
        return queryset.filter(query)
