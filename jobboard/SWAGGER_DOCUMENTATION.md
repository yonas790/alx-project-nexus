# Swagger Documentation - Job Board API

## 📚 Complete API Documentation

The Job Board API includes comprehensive Swagger/OpenAPI documentation that provides an interactive interface for testing all API endpoints.

## 🔗 Documentation URLs

Once the server is running (`python manage.py runserver`), access the documentation at:

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

### API Schema
- **OpenAPI JSON**: http://localhost:8000/api/swagger.json

## 🔐 Authentication in Swagger

### Step 1: Login to Get Token
```json
POST /api/auth/login/
{
  "username": "testuser",
  "password": "testpass123"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Step 2: Use Token in Swagger
1. Click **Authorize** button in Swagger UI
2. Enter: `Bearer <your_access_token>`
3. Click **Authorize**
4. Now test protected endpoints

## 📊 API Endpoints Documentation

### 🔓 Public Endpoints (No Authentication)

#### Jobs
- **GET /api/jobs/** - List all active jobs with filtering
- **GET /api/jobs/{slug}/** - Get job details by slug

#### Categories
- **GET /api/categories/** - List all job categories
- **GET /api/categories/{id}/** - Get category details

#### Companies
- **GET /api/companies/** - List all companies
- **GET /api/companies/{id}/** - Get company details

#### Job Types
- **GET /api/job-types/** - List all job types
- **GET /api/job-types/{id}/** - Get job type details

#### Statistics
- **GET /api/statistics/** - Get job board statistics

### 🔒 Protected Endpoints (Authentication Required)

#### Authentication
- **POST /api/auth/login/** - User login (get JWT tokens)
- **POST /api/auth/refresh/** - Refresh JWT token

#### Job Management
- **POST /api/jobs/create/** - Create new job posting
- **PUT /api/jobs/{slug}/** - Update job posting
- **DELETE /api/jobs/{slug}/** - Delete job posting

#### Applications
- **GET /api/applications/** - List user applications
- **POST /api/applications/** - Submit job application
- **GET /api/applications/{id}/** - Get application details
- **PUT /api/applications/{id}/** - Update application
- **DELETE /api/applications/{id}/** - Delete application

#### Saved Jobs
- **GET /api/saved-jobs/** - List user's saved jobs
- **POST /api/saved-jobs/** - Save a job
- **DELETE /api/saved-jobs/{id}/** - Remove saved job

#### Job Alerts
- **GET /api/job-alerts/** - List user's job alerts
- **POST /api/job-alerts/** - Create job alert
- **GET /api/job-alerts/{id}/** - Get job alert details
- **PUT /api/job-alerts/{id}/** - Update job alert
- **DELETE /api/job-alerts/{id}/** - Delete job alert

## 🔍 Advanced Search & Filtering

### Search Parameters
The `/api/jobs/` endpoint supports advanced filtering:

#### Text Search
- **search**: Search across title, description, company, location, tags
- **Example**: `GET /api/jobs/?search=python`

#### Category & Company
- **category**: Filter by category ID
- **company**: Filter by company ID
- **Example**: `GET /api/jobs/?category=1&company=2`

#### Location & Remote
- **location**: Filter by location (partial match)
- **is_remote**: Filter remote jobs (true/false)
- **Example**: `GET /api/jobs/?location=remote&is_remote=true`

#### Salary Range
- **salary_min**: Minimum salary filter
- **salary_max**: Maximum salary filter
- **Example**: `GET /api/jobs/?salary_min=50000&salary_max=100000`

#### Experience & Job Type
- **experience_level**: entry, mid, senior, executive
- **job_type**: Filter by job type ID
- **Example**: `GET /api/jobs/?experience_level=senior&job_type=1`

#### Tags
- **tags**: Comma-separated tag filtering
- **Example**: `GET /api/jobs/?tags=python,django,api`

#### Ordering
- **ordering**: Sort by field (created_at, title, salary_min, etc.)
- **Example**: `GET /api/jobs/?ordering=-created_at`

### Combined Search Example
```bash
GET /api/jobs/?search=developer&location=remote&category=1&salary_min=80000&experience_level=senior&ordering=-created_at
```

## 📝 Request/Response Examples

### Create Job Posting
```json
POST /api/jobs/create/
{
  "title": "Senior Python Developer",
  "description": "We are looking for an experienced Python developer...",
  "requirements": "5+ years Python experience, Django knowledge...",
  "responsibilities": "Develop and maintain backend services...",
  "benefits": "Health insurance, 401k, flexible hours...",
  "company": 1,
  "category": 1,
  "job_type": 1,
  "location": "San Francisco, CA",
  "is_remote": true,
  "salary_min": 120000,
  "salary_max": 160000,
  "currency": "USD",
  "experience_level": "senior",
  "status": "active",
  "tags": "python, django, api, backend, senior"
}
```

### Submit Job Application
```json
POST /api/applications/
{
  "job_id": 1,
  "cover_letter": "I am excited to apply for this position...",
  "phone": "+1234567890",
  "email": "applicant@example.com",
  "linkedin_url": "https://linkedin.com/in/applicant",
  "portfolio_url": "https://portfolio.example.com",
  "expected_salary": 140000,
  "availability_date": "2024-02-01"
}
```

### Create Job Alert
```json
POST /api/job-alerts/
{
  "name": "Python Developer Alert",
  "keywords": "python, django, backend",
  "category_ids": [1, 2],
  "locations": "San Francisco, Remote",
  "job_type_ids": [1, 2],
  "experience_levels": "mid,senior",
  "salary_min": 80000,
  "is_remote": true,
  "frequency": "weekly"
}
```

## 🧪 Testing in Swagger UI

### Interactive Features
1. **Try it out**: Click on any endpoint to test
2. **Parameter Input**: Fill in request parameters
3. **Authentication**: Use JWT tokens for protected endpoints
4. **Response Viewing**: See actual API responses
5. **Schema Validation**: Request/response validation

### Testing Workflow
1. **Start Server**: `python manage.py runserver`
2. **Open Swagger**: Go to http://localhost:8000/api/docs/
3. **Authenticate**: Use login endpoint to get JWT token
4. **Authorize**: Click Authorize and enter Bearer token
5. **Test Endpoints**: Try all endpoints interactively

## 📊 Response Examples

### Job List Response
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/jobs/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Senior Python Developer",
      "company": {
        "id": 1,
        "name": "TechCorp Solutions",
        "location": "San Francisco, CA"
      },
      "category": {
        "id": 1,
        "name": "Software Development"
      },
      "job_type": {
        "id": 1,
        "name": "Full-time"
      },
      "location": "San Francisco, CA",
      "is_remote": true,
      "salary_min": "120000.00",
      "salary_max": "160000.00",
      "currency": "USD",
      "experience_level": "senior",
      "status": "active",
      "created_at": "2024-01-15T10:30:00Z",
      "views_count": 45,
      "applications_count": 8
    }
  ]
}
```

### Statistics Response
```json
{
  "total_jobs": 25,
  "total_companies": 5,
  "total_applications": 150,
  "total_categories": 8,
  "jobs_by_category": [
    {"name": "Software Development", "job_count": 12},
    {"name": "Data Science", "job_count": 5},
    {"name": "Marketing", "job_count": 3}
  ],
  "jobs_by_location": [
    {"location": "San Francisco, CA", "count": 8},
    {"location": "Remote", "count": 6},
    {"location": "New York, NY", "count": 4}
  ],
  "average_salary": "95000.00"
}
```

## 🔧 Error Handling

### HTTP Status Codes
- **200 OK**: Successful request
- **201 Created**: Resource created successfully
- **400 Bad Request**: Invalid request data
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

### Error Response Format
```json
{
  "error": "Error message",
  "details": "Detailed error information",
  "field_errors": {
    "field_name": ["Field-specific error message"]
  }
}
```

## 🚀 Production Considerations

### Security
- Use HTTPS in production
- Set secure JWT secret keys
- Configure proper CORS settings
- Implement rate limiting

### Performance
- Enable Redis caching
- Use database connection pooling
- Implement query optimization
- Set up monitoring

### Documentation
- Keep API documentation updated
- Version your API endpoints
- Provide migration guides
- Document breaking changes

## 📞 Support

### Common Issues
1. **Authentication Errors**: Check JWT token format and expiration
2. **Permission Errors**: Verify user roles and permissions
3. **Validation Errors**: Check request data format
4. **Connection Errors**: Verify server is running

### Getting Help
1. Check the Swagger UI for interactive testing
2. Review the API documentation
3. Test with sample data
4. Check server logs for errors

---

**Happy API Testing! 🚀**

The Swagger documentation provides a complete, interactive interface for testing all Job Board API endpoints with proper authentication and comprehensive examples.
