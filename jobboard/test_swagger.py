#!/usr/bin/env python
"""
Test script to verify Swagger documentation is working
Run this after starting the Django server
"""

import requests
import json

def test_swagger_endpoints():
    """Test that Swagger documentation endpoints are accessible"""
    base_url = "http://localhost:8000"
    
    endpoints = [
        "/api/docs/",
        "/api/redoc/", 
        "/api/swagger.json",
        "/api/jobs/",
        "/api/categories/",
        "/api/companies/",
        "/api/statistics/"
    ]
    
    print("🧪 Testing Swagger Documentation Endpoints")
    print("=" * 50)
    
    for endpoint in endpoints:
        try:
            url = f"{base_url}{endpoint}"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"✅ {endpoint} - OK ({response.status_code})")
            else:
                print(f"⚠️  {endpoint} - Status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {endpoint} - Connection Error (Server not running?)")
        except Exception as e:
            print(f"❌ {endpoint} - Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("📚 Swagger Documentation URLs:")
    print(f"🔗 Swagger UI: {base_url}/api/docs/")
    print(f"🔗 ReDoc: {base_url}/api/redoc/")
    print(f"🔗 OpenAPI JSON: {base_url}/api/swagger.json")
    print("\n💡 Make sure the Django server is running:")
    print("   python manage.py runserver")

def test_api_functionality():
    """Test basic API functionality"""
    base_url = "http://localhost:8000"
    
    print("\n🔍 Testing API Functionality")
    print("=" * 50)
    
    # Test public endpoints
    try:
        # Test jobs endpoint
        response = requests.get(f"{base_url}/api/jobs/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Jobs API - Found {len(data.get('results', []))} jobs")
        else:
            print(f"⚠️  Jobs API - Status {response.status_code}")
            
        # Test statistics endpoint
        response = requests.get(f"{base_url}/api/statistics/")
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ Statistics API - Total jobs: {stats.get('total_jobs', 0)}")
        else:
            print(f"⚠️  Statistics API - Status {response.status_code}")
            
    except Exception as e:
        print(f"❌ API Test Error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Job Board API - Swagger Documentation Test")
    print("=" * 60)
    
    test_swagger_endpoints()
    test_api_functionality()
    
    print("\n🎯 Next Steps:")
    print("1. Start the server: python manage.py runserver")
    print("2. Open Swagger UI: http://localhost:8000/api/docs/")
    print("3. Test authentication: POST /api/auth/login/")
    print("4. Explore all endpoints in the interactive interface")
    print("\n📖 For detailed setup instructions, see SWAGGER_SETUP_GUIDE.md")
