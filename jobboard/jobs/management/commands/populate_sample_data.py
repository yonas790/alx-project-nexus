from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from jobs.models import Category, Company, JobType, Job
from decimal import Decimal
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Software Development', 'description': 'Programming and software engineering roles'},
            {'name': 'Data Science', 'description': 'Data analysis, machine learning, and AI roles'},
            {'name': 'Marketing', 'description': 'Digital marketing, content creation, and advertising'},
            {'name': 'Design', 'description': 'UI/UX design, graphic design, and creative roles'},
            {'name': 'Sales', 'description': 'Sales and business development positions'},
            {'name': 'Operations', 'description': 'Operations, logistics, and supply chain management'},
            {'name': 'Finance', 'description': 'Accounting, financial analysis, and investment roles'},
            {'name': 'Human Resources', 'description': 'HR, recruitment, and people operations'},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create job types
        job_types_data = [
            {'name': 'Full-time', 'description': 'Permanent full-time employment'},
            {'name': 'Part-time', 'description': 'Part-time employment'},
            {'name': 'Contract', 'description': 'Contract-based work'},
            {'name': 'Freelance', 'description': 'Freelance and project-based work'},
            {'name': 'Internship', 'description': 'Internship and entry-level positions'},
        ]
        
        job_types = []
        for jt_data in job_types_data:
            job_type, created = JobType.objects.get_or_create(
                name=jt_data['name'],
                defaults={'description': jt_data['description']}
            )
            job_types.append(job_type)
            if created:
                self.stdout.write(f'Created job type: {job_type.name}')

        # Create companies
        companies_data = [
            {
                'name': 'TechCorp Solutions',
                'description': 'Leading technology company specializing in cloud solutions',
                'website': 'https://techcorp.com',
                'location': 'San Francisco, CA',
                'size': '500-1000',
                'industry': 'Technology'
            },
            {
                'name': 'DataFlow Inc',
                'description': 'Data analytics and machine learning company',
                'website': 'https://dataflow.com',
                'location': 'New York, NY',
                'size': '100-500',
                'industry': 'Data Science'
            },
            {
                'name': 'Creative Agency',
                'description': 'Full-service digital marketing and design agency',
                'website': 'https://creativeagency.com',
                'location': 'Los Angeles, CA',
                'size': '50-100',
                'industry': 'Marketing'
            },
            {
                'name': 'FinanceFirst',
                'description': 'Financial services and investment management',
                'website': 'https://financefirst.com',
                'location': 'Chicago, IL',
                'size': '1000+',
                'industry': 'Finance'
            },
            {
                'name': 'StartupXYZ',
                'description': 'Innovative startup in the fintech space',
                'website': 'https://startupxyz.com',
                'location': 'Austin, TX',
                'size': '10-50',
                'industry': 'Technology'
            },
        ]
        
        companies = []
        for comp_data in companies_data:
            company, created = Company.objects.get_or_create(
                name=comp_data['name'],
                defaults=comp_data
            )
            companies.append(company)
            if created:
                self.stdout.write(f'Created company: {company.name}')

        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'is_staff': True
            }
        )
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write('Created test user: testuser')

        # Create sample jobs
        jobs_data = [
            {
                'title': 'Senior Python Developer',
                'description': 'We are looking for an experienced Python developer to join our backend team. You will work on building scalable APIs and microservices.',
                'requirements': '5+ years Python experience, Django/FastAPI knowledge, PostgreSQL, Docker, AWS',
                'responsibilities': 'Develop and maintain backend services, collaborate with frontend team, optimize database queries',
                'benefits': 'Health insurance, 401k, flexible hours, remote work options',
                'company': companies[0],
                'category': categories[0],
                'job_type': job_types[0],
                'location': 'San Francisco, CA',
                'is_remote': True,
                'salary_min': Decimal('120000'),
                'salary_max': Decimal('160000'),
                'experience_level': 'senior',
                'status': 'active',
                'tags': 'python, django, api, backend, senior'
            },
            {
                'title': 'Data Scientist',
                'description': 'Join our data science team to build machine learning models and analyze large datasets.',
                'requirements': 'PhD in Data Science or related field, Python, R, TensorFlow, SQL, statistics',
                'responsibilities': 'Build ML models, analyze data, create visualizations, collaborate with engineering team',
                'benefits': 'Competitive salary, stock options, learning budget',
                'company': companies[1],
                'category': categories[1],
                'job_type': job_types[0],
                'location': 'New York, NY',
                'is_remote': False,
                'salary_min': Decimal('100000'),
                'salary_max': Decimal('140000'),
                'experience_level': 'mid',
                'status': 'active',
                'tags': 'data-science, machine-learning, python, statistics'
            },
            {
                'title': 'Frontend Developer',
                'description': 'Create beautiful and responsive user interfaces using modern web technologies.',
                'requirements': '3+ years React experience, TypeScript, CSS, HTML, Git',
                'responsibilities': 'Build user interfaces, optimize performance, collaborate with designers',
                'benefits': 'Flexible schedule, health benefits, professional development',
                'company': companies[2],
                'category': categories[0],
                'job_type': job_types[0],
                'location': 'Los Angeles, CA',
                'is_remote': True,
                'salary_min': Decimal('80000'),
                'salary_max': Decimal('110000'),
                'experience_level': 'mid',
                'status': 'active',
                'tags': 'react, frontend, javascript, typescript, ui'
            },
            {
                'title': 'Marketing Manager',
                'description': 'Lead our marketing efforts and develop strategies to grow our customer base.',
                'requirements': '5+ years marketing experience, digital marketing, analytics, team leadership',
                'responsibilities': 'Develop marketing strategies, manage campaigns, analyze performance, lead team',
                'benefits': 'Health insurance, 401k, bonus potential, flexible hours',
                'company': companies[2],
                'category': categories[2],
                'job_type': job_types[0],
                'location': 'Los Angeles, CA',
                'is_remote': False,
                'salary_min': Decimal('70000'),
                'salary_max': Decimal('95000'),
                'experience_level': 'senior',
                'status': 'active',
                'tags': 'marketing, digital-marketing, strategy, management'
            },
            {
                'title': 'DevOps Engineer',
                'description': 'Manage our cloud infrastructure and deployment pipelines.',
                'requirements': '3+ years DevOps experience, AWS, Docker, Kubernetes, CI/CD',
                'responsibilities': 'Manage cloud infrastructure, automate deployments, monitor systems',
                'benefits': 'Competitive salary, health benefits, remote work',
                'company': companies[4],
                'category': categories[0],
                'job_type': job_types[0],
                'location': 'Austin, TX',
                'is_remote': True,
                'salary_min': Decimal('90000'),
                'salary_max': Decimal('130000'),
                'experience_level': 'mid',
                'status': 'active',
                'tags': 'devops, aws, docker, kubernetes, infrastructure'
            },
            {
                'title': 'UI/UX Designer',
                'description': 'Design intuitive and beautiful user experiences for our products.',
                'requirements': '3+ years design experience, Figma, Adobe Creative Suite, user research',
                'responsibilities': 'Create wireframes, design interfaces, conduct user research, collaborate with developers',
                'benefits': 'Creative freedom, health benefits, design tools budget',
                'company': companies[2],
                'category': categories[3],
                'job_type': job_types[0],
                'location': 'Los Angeles, CA',
                'is_remote': True,
                'salary_min': Decimal('65000'),
                'salary_max': Decimal('90000'),
                'experience_level': 'mid',
                'status': 'active',
                'tags': 'ui, ux, design, figma, user-research'
            },
            {
                'title': 'Sales Representative',
                'description': 'Drive sales growth by building relationships with new and existing clients.',
                'requirements': '2+ years sales experience, communication skills, CRM experience',
                'responsibilities': 'Generate leads, close deals, maintain client relationships, meet targets',
                'benefits': 'Commission structure, health benefits, car allowance',
                'company': companies[3],
                'category': categories[4],
                'job_type': job_types[0],
                'location': 'Chicago, IL',
                'is_remote': False,
                'salary_min': Decimal('50000'),
                'salary_max': Decimal('80000'),
                'experience_level': 'entry',
                'status': 'active',
                'tags': 'sales, business-development, crm, communication'
            },
            {
                'title': 'Financial Analyst',
                'description': 'Analyze financial data and provide insights to support business decisions.',
                'requirements': 'Bachelor in Finance, Excel, financial modeling, analytical skills',
                'responsibilities': 'Analyze financial data, create reports, support budgeting, risk assessment',
                'benefits': 'Health insurance, 401k, professional development, bonus potential',
                'company': companies[3],
                'category': categories[6],
                'job_type': job_types[0],
                'location': 'Chicago, IL',
                'is_remote': False,
                'salary_min': Decimal('60000'),
                'salary_max': Decimal('85000'),
                'experience_level': 'entry',
                'status': 'active',
                'tags': 'finance, analysis, excel, modeling, reporting'
            },
        ]
        
        for job_data in jobs_data:
            job_data['posted_by'] = user
            job_data['expires_at'] = datetime.now() + timedelta(days=30)
            
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults=job_data
            )
            if created:
                self.stdout.write(f'Created job: {job.title} at {job.company.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write(f'Created {len(categories)} categories')
        self.stdout.write(f'Created {len(job_types)} job types')
        self.stdout.write(f'Created {len(companies)} companies')
        self.stdout.write(f'Created {len(jobs_data)} jobs')
        self.stdout.write('Test user: testuser / testpass123')
