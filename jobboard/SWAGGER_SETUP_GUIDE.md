# Swagger Documentation Setup Guide

## 🚀 Quick Start for Swagger Documentation

The Job Board API includes comprehensive Swagger/OpenAPI documentation that provides an interactive interface for testing all API endpoints.

## 📋 Prerequisites

### 1. Python Installation
```bash
# Download and install Python 3.8+ from https://python.org
# Make sure to check "Add Python to PATH" during installation
```

### 2. Virtual Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🗄 Database Setup

### Option 1: PostgreSQL (Recommended)
```bash
# Install PostgreSQL and create database
createdb jobboard_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Option 2: SQLite (Quick Start)
```python
# In settings.py, change database to:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 🚀 Running the Server

```bash
# Start the development server
python manage.py runserver
```

The server will start at `http://localhost:8000`

## 📚 Accessing Swagger Documentation

### 1. Swagger UI (Interactive)
- **URL**: http://localhost:8000/api/docs/
- **Features**: Interactive API testing, authentication, request/response examples
- **Authentication**: Use JWT tokens for protected endpoints

### 2. ReDoc (Alternative Documentation)
- **URL**: http://localhost:8000/api/redoc/
- **Features**: Clean, readable documentation format

### 3. OpenAPI JSON Schema
- **URL**: http://localhost:8000/api/swagger.json
- **Features**: Raw OpenAPI specification for integration

## 🔐 Authentication in Swagger

### Step 1: Get Authentication Token
1. Go to `/api/docs/`
2. Find the **Authentication** section
3. Click **Authorize** button
4. Use the login endpoint to get tokens:

```json
POST /api/auth/login/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Step 2: Use Token in Swagger
1. Copy the `access` token from the login response
2. Click **Authorize** in Swagger UI
3. Enter: `Bearer <your_access_token>`
4. Click **Authorize**
5. Now you can test protected endpoints

## 📊 Sample Data Setup

### Populate Sample Data
```bash
# Run the management command to create sample data
python manage.py populate_sample_data
```

This will create:
- 8 job categories
- 5 companies
- 5 job types
- 8 sample jobs
- Test user: `testuser` / `testpass123`

## 🧪 Testing API Endpoints

### 1. Public Endpoints (No Authentication Required)
- `GET /api/jobs/` - List all active jobs
- `GET /api/jobs/{slug}/` - Get job details
- `GET /api/categories/` - List categories
- `GET /api/companies/` - List companies
- `GET /api/statistics/` - Get job board statistics

### 2. Protected Endpoints (Authentication Required)
- `POST /api/jobs/create/` - Create new job
- `GET /api/applications/` - List user applications
- `POST /api/applications/` - Submit job application
- `POST /api/auth/login/` - User login
- `POST /api/auth/refresh/` - Refresh token

### 3. Advanced Search Examples
```bash
# Search for Python jobs
GET /api/jobs/?search=python

# Filter by location
GET /api/jobs/?location=remote

# Filter by category
GET /api/jobs/?category=1

# Filter by salary range
GET /api/jobs/?salary_min=50000&salary_max=100000

# Multiple filters
GET /api/jobs/?search=developer&location=remote&salary_min=80000
```

## 🔍 Swagger Features

### Interactive Testing
- **Try it out**: Click on any endpoint to test
- **Request/Response**: See actual API responses
- **Authentication**: Test with JWT tokens
- **Parameters**: Easy parameter input
- **Schema**: View request/response schemas

### Documentation Features
- **Complete API Coverage**: All endpoints documented
- **Authentication Support**: JWT token integration
- **Request Examples**: Detailed request/response examples
- **Error Handling**: HTTP status codes and error responses
- **Schema Validation**: Request/response validation

## 🐳 Docker Setup (Alternative)

### Quick Docker Setup
```bash
# Build and run with Docker Compose
docker-compose up -d

# Access the application
# API: http://localhost:8000
# Swagger: http://localhost:8000/api/docs/
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Python Not Found
```bash
# Install Python from https://python.org
# Make sure to add to PATH during installation
```

#### 2. Database Connection Error
```bash
# For SQLite (quick start):
# Change DATABASES in settings.py to use SQLite
# Then run: python manage.py migrate
```

#### 3. Import Errors
```bash
# Make sure all dependencies are installed:
pip install -r requirements.txt
```

#### 4. Swagger Not Loading
```bash
# Check if drf-yasg is installed:
pip install drf-yasg

# Restart the server:
python manage.py runserver
```

## 📱 Mobile/API Testing

### Using Postman
1. Import the OpenAPI schema from `/api/swagger.json`
2. Set up authentication with JWT tokens
3. Test all endpoints with proper headers

### Using curl
```bash
# Get authentication token
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'

# Use token for protected endpoints
curl -X GET http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <your_token>"
```

## 🎯 Production Deployment

### Environment Variables
```bash
# Set production environment variables
export DEBUG=False
export SECRET_KEY=your-production-secret-key
export DB_NAME=jobboard_prod
export DB_USER=postgres
export DB_PASSWORD=secure-password
export DB_HOST=your-db-host
export REDIS_URL=redis://your-redis-host:6379/1
```

### Security Considerations
- Change default SECRET_KEY
- Use environment variables for sensitive data
- Configure proper CORS settings
- Set up SSL certificates
- Use production database

## 📊 API Documentation Features

### Comprehensive Coverage
- **All Endpoints**: Complete API documentation
- **Authentication**: JWT token integration
- **Request/Response**: Detailed schemas
- **Error Handling**: HTTP status codes
- **Examples**: Real request/response examples

### Interactive Features
- **Try it out**: Test endpoints directly
- **Authentication**: Secure token testing
- **Parameter Input**: Easy form-based input
- **Response Viewing**: See actual API responses
- **Schema Validation**: Request validation

## 🚀 Next Steps

1. **Start the server**: `python manage.py runserver`
2. **Access Swagger**: Go to `http://localhost:8000/api/docs/`
3. **Test endpoints**: Use the interactive interface
4. **Authenticate**: Get JWT tokens for protected endpoints
5. **Explore features**: Test all API functionality

## 📞 Support

If you encounter any issues:
1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure database is properly configured
4. Check the README.md for detailed setup instructions

---

**Happy API Testing! 🚀**
