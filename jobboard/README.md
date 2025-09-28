# Job Board Backend API

A comprehensive job board backend API built with Django REST Framework, featuring advanced job search, role-based authentication, and optimized database queries.

## 🚀 Features

### Core Functionality
- **Job Management**: Create, read, update, and delete job postings
- **Company Management**: Manage company profiles and information
- **Category System**: Organize jobs by industry and type
- **Application System**: Handle job applications with status tracking
- **User Management**: Role-based access control for admins and users

### Advanced Features
- **Advanced Search**: Multi-criteria job search with filtering
- **Job Analytics**: Track views, applications, and engagement metrics
- **Saved Jobs**: Allow users to save jobs for later
- **Job Alerts**: Email notifications for matching job criteria
- **Caching**: Redis-based caching for improved performance
- **API Documentation**: Comprehensive Swagger/OpenAPI documentation

### Technical Features
- **JWT Authentication**: Secure token-based authentication
- **Database Optimization**: Indexed queries and optimized database design
- **CORS Support**: Cross-origin resource sharing for frontend integration
- **File Upload**: Support for resume and company logo uploads
- **Pagination**: Efficient data pagination for large datasets

## 🛠 Technology Stack

- **Backend**: Django 5.2.6 + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Caching**: Redis
- **Documentation**: Swagger/OpenAPI
- **Deployment**: Gunicorn + WhiteNoise

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis (optional, for caching)
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd jobboard
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=jobboard_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://127.0.0.1:6379/1
```

### 5. Database Setup
```bash
# Create PostgreSQL database
createdb jobboard_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 6. Load Sample Data (Optional)
```bash
python manage.py loaddata fixtures/sample_data.json
```

### 7. Run Development Server
```bash
python manage.py runserver
```

## 📚 API Documentation

Once the server is running, access the API documentation at:
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

## 🔐 Authentication

The API uses JWT authentication. To authenticate:

1. **Login**: `POST /api/auth/login/`
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Use Token**: Include the token in the Authorization header:
   ```
   Authorization: Bearer <your_access_token>
   ```

3. **Refresh Token**: `POST /api/auth/refresh/`
   ```json
   {
     "refresh": "your_refresh_token"
   }
   ```

## 📊 API Endpoints

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create category (authenticated)
- `GET /api/categories/{id}/` - Get category details
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

### Companies
- `GET /api/companies/` - List all companies
- `POST /api/companies/` - Create company (authenticated)
- `GET /api/companies/{id}/` - Get company details
- `PUT /api/companies/{id}/` - Update company
- `DELETE /api/companies/{id}/` - Delete company

### Jobs
- `GET /api/jobs/` - List active jobs (with filtering)
- `GET /api/jobs/{slug}/` - Get job details
- `POST /api/jobs/create/` - Create job (authenticated)
- `GET /api/statistics/` - Get job board statistics

### Applications
- `GET /api/applications/` - List user applications
- `POST /api/applications/` - Submit application (authenticated)

## 🔍 Advanced Search

The job search supports multiple filters:

```bash
GET /api/jobs/?search=python&location=remote&category=1&salary_min=50000
```

### Available Filters:
- `search`: Text search across title, description, company
- `category`: Filter by category ID
- `location`: Filter by location (partial match)
- `job_type`: Filter by job type ID
- `experience_level`: entry, mid, senior, executive
- `is_remote`: true/false
- `salary_min`: Minimum salary
- `salary_max`: Maximum salary
- `tags`: Comma-separated tags
- `ordering`: Sort by field (created_at, title, salary_min, etc.)

## 🗄 Database Schema

### Core Models

#### Job
- Basic job information (title, description, requirements)
- Company and category relationships
- Location and salary details
- Status and expiration tracking
- Analytics (views, applications count)

#### Application
- Job and applicant relationships
- Application details (cover letter, resume)
- Status tracking (pending, reviewed, etc.)
- Contact information

#### Company
- Company profile information
- Industry and location details
- Logo and website links

#### Category
- Job categories and descriptions
- Hierarchical organization support

## 🚀 Deployment

### Production Settings
1. Set `DEBUG=False` in environment variables
2. Configure production database
3. Set up Redis for caching
4. Configure static file serving
5. Set up SSL certificates

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d
```

### Environment Variables
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
DB_NAME=jobboard_prod
DB_USER=postgres
DB_PASSWORD=secure-password
DB_HOST=db-host
DB_PORT=5432
REDIS_URL=redis://redis-host:6379/1
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📈 Performance Optimization

### Database Indexing
- Indexed fields for fast queries
- Composite indexes for common filter combinations
- Foreign key indexes for relationships

### Caching Strategy
- Redis caching for frequently accessed data
- Query result caching
- Session caching

### Query Optimization
- Select related for foreign keys
- Prefetch related for many-to-many relationships
- Pagination for large datasets

## 🔒 Security Features

- JWT token authentication
- Role-based permissions
- CORS configuration
- Input validation and sanitization
- SQL injection prevention
- XSS protection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation
- Review the code comments and docstrings

## 🎯 Future Enhancements

- [ ] Email notifications for job alerts
- [ ] Advanced analytics dashboard
- [ ] Job recommendation engine
- [ ] Social login integration
- [ ] Mobile app API endpoints
- [ ] Real-time notifications
- [ ] Advanced search with Elasticsearch
- [ ] Job application tracking system
- [ ] Company verification system
- [ ] API rate limiting

---

**Built with ❤️ for the ProDev Backend Program**
