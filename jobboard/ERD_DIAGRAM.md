# Job Board Database ERD

## Entity Relationship Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     User        │    │    Category     │    │    Company      │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │    │ id (PK)         │    │ id (PK)         │
│ username        │    │ name            │    │ name            │
│ email           │    │ description     │    │ description     │
│ first_name      │    │ created_at      │    │ website         │
│ last_name       │    │ updated_at      │    │ logo            │
│ is_staff        │    └─────────────────┘    │ location        │
│ date_joined     │                           │ size            │
└─────────────────┘                           │ industry        │
         │                                   │ created_at      │
         │                                   │ updated_at      │
         │                                   └─────────────────┘
         │                                            │
         │                                            │
         │ 1:N                                        │ 1:N
         │                                            │
         ▼                                            ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Job         │    │   JobType       │    │  Application    │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │    │ id (PK)         │    │ id (PK)         │
│ title           │    │ name            │    │ job_id (FK)     │
│ description     │    │ description     │    │ applicant_id(FK)│
│ requirements    │    └─────────────────┘    │ cover_letter    │
│ responsibilities│                           │ resume          │
│ benefits        │                           │ status          │
│ company_id (FK) │                           │ phone           │
│ category_id (FK)│                           │ email           │
│ job_type_id (FK)│                           │ linkedin_url    │
│ posted_by_id(FK)│                           │ portfolio_url   │
│ location        │                           │ expected_salary │
│ is_remote       │                           │ availability_date│
│ salary_min      │                           │ notes           │
│ salary_max      │                           │ applied_at      │
│ currency        │                           │ updated_at      │
│ experience_level│                           │ reviewed_at     │
│ status          │                           └─────────────────┘
│ created_at      │
│ updated_at      │
│ expires_at      │
│ slug            │
│ tags            │
│ views_count     │
│ applications_count│
└─────────────────┘
         │
         │ 1:N
         │
         ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   JobView       │    │   SavedJob      │    │   JobAlert      │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │    │ id (PK)         │    │ id (PK)         │
│ job_id (FK)     │    │ user_id (FK)    │    │ user_id (FK)    │
│ user_id (FK)    │    │ job_id (FK)     │    │ name            │
│ ip_address      │    │ saved_at        │    │ keywords        │
│ user_agent      │    └─────────────────┘    │ locations       │
│ viewed_at       │                           │ experience_levels│
└─────────────────┘                           │ salary_min      │
                                               │ is_remote       │
                                               │ frequency       │
                                               │ is_active       │
                                               │ created_at      │
                                               │ last_sent       │
                                               └─────────────────┘
```

## Relationships

### One-to-Many Relationships:
1. **User → Job**: One user can post many jobs
2. **Company → Job**: One company can have many jobs
3. **Category → Job**: One category can have many jobs
4. **JobType → Job**: One job type can have many jobs
5. **User → Application**: One user can have many applications
6. **Job → Application**: One job can have many applications
7. **User → JobView**: One user can view many jobs
8. **Job → JobView**: One job can be viewed many times
9. **User → SavedJob**: One user can save many jobs
10. **Job → SavedJob**: One job can be saved by many users
11. **User → JobAlert**: One user can have many job alerts

### Many-to-Many Relationships:
1. **JobAlert ↔ Category**: Job alerts can be associated with multiple categories
2. **JobAlert ↔ JobType**: Job alerts can be associated with multiple job types

## Key Features

### Database Indexes:
- **Job**: title, location, status, experience_level, created_at, expires_at
- **Application**: status, applied_at, job_id, applicant_id
- **JobView**: job_id, viewed_at, ip_address
- **Category**: name
- **Company**: name, industry

### Constraints:
- **Unique**: Application(job, applicant) - prevents duplicate applications
- **Unique**: SavedJob(user, job) - prevents duplicate saved jobs
- **Unique**: Job.slug - ensures unique job URLs
- **Unique**: Category.name - ensures unique category names
- **Unique**: JobType.name - ensures unique job type names

### Business Rules:
1. Jobs have expiration dates
2. Applications are unique per user per job
3. Saved jobs are unique per user per job
4. Job views are tracked for analytics
5. Job alerts can be customized with multiple criteria
6. Salary validation (min ≤ max)
7. Expiration date must be in the future

## Performance Optimizations

### Query Optimization:
- **Select Related**: For foreign key relationships
- **Prefetch Related**: For many-to-many relationships
- **Database Indexes**: On frequently queried fields
- **Composite Indexes**: For common filter combinations

### Caching Strategy:
- **Redis Caching**: For frequently accessed data
- **Query Result Caching**: For expensive queries
- **Session Caching**: For user sessions

### Scalability Features:
- **Pagination**: For large result sets
- **Filtering**: For efficient data retrieval
- **Search**: Full-text search capabilities
- **Analytics**: View tracking and statistics
