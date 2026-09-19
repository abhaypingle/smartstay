# SmartStay — Entity Relationship Diagram

This diagram represents the core database schema for SmartStay, as designed in Phase 4.

```mermaid
erDiagram
  USERS ||--o| OWNER_PROFILES : has
  USERS ||--o{ PROPERTIES : owns
  PROPERTIES ||--o{ ROOMS : has
  PROPERTIES ||--o{ PROPERTY_IMAGES : has
  PROPERTIES ||--o{ PROPERTY_AMENITIES : has
  AMENITIES ||--o{ PROPERTY_AMENITIES : has
  USERS ||--o{ FAVORITES : saves
  PROPERTIES ||--o{ FAVORITES : saved_in
  USERS ||--o{ VISIT_REQUESTS : makes
  PROPERTIES ||--o{ VISIT_REQUESTS : receives
  USERS ||--o{ REPORTS : files
  PROPERTIES ||--o{ REPORTS : about

  USERS {
    int id PK
    string name
    string email
    string password_hash
    string role
    string phone
    timestamp created_at
    timestamp updated_at
  }
  OWNER_PROFILES {
    int id PK
    int user_id FK
    string business_name
    boolean verified
    text bio
  }
  PROPERTIES {
    int id PK
    int owner_id FK
    string title
    text description
    string accommodation_type
    string room_type
    int rent
    int deposit
    int maintenance
    string furnishing
    string city
    string address
    float latitude
    float longitude
    string status
    boolean verified
    timestamp created_at
    timestamp updated_at
  }
  ROOMS {
    int id PK
    int property_id FK
    string room_type
    int rent_override
    boolean available
  }
  PROPERTY_IMAGES {
    int id PK
    int property_id FK
    string image_url
    boolean is_primary
  }
  AMENITIES {
    int id PK
    string name
  }
  PROPERTY_AMENITIES {
    int property_id FK
    int amenity_id FK
  }
  FAVORITES {
    int id PK
    int user_id FK
    int property_id FK
    timestamp created_at
  }
  VISIT_REQUESTS {
    int id PK
    int user_id FK
    int property_id FK
    date requested_date
    string status
    timestamp created_at
  }
  REPORTS {
    int id PK
    int reporter_id FK
    int property_id FK
    text reason
    string status
    timestamp created_at
  }
```

## Notes

- **users** is the shared base table for all roles (tenant, owner, admin), distinguished by the `role` field.
- **owner_profiles** extends `users` with owner-specific fields, only populated when `role = 'owner'`.
- **property_amenities** is a join table implementing the many-to-many relationship between `properties` and `amenities`.
- Admin does not have a dedicated table for now — the `role = 'admin'` flag on `users` is sufficient.
- All foreign keys reference the primary key of their related table (e.g. `owner_id` in `properties` references `users.id`).