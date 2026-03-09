# Microservices Architecture

The StudyConnect platform is implemented using a microservices architecture where each service is responsible for a specific domain of functionality. Services communicate through REST APIs via the API Gateway, and each service maintains its own database to ensure loose coupling and independent scalability.

## Services

### API Gateway
The API Gateway acts as the single entry point for all client requests. It routes incoming HTTP requests from the frontend to the correct microservice, performs request validation, enforces authentication tokens, and handles rate limiting and logging.

### Auth Service
The Auth Service manages user authentication and security. It handles user registration, login verification, password hashing, JWT token generation, and token validation for protected endpoints across the platform.

### User Service
The User Service manages student and tutor profile data. It stores personal information, enrolled courses, and profile preferences. It also provides APIs for updating profile information and retrieving user details for other services such as study group membership.

### Study Group Service
The Study Group Service handles all group collaboration features. It allows users to create study groups, join or leave groups, manage group memberships, and retrieve lists of groups associated with specific courses.

### Resource Service
The Resource Service manages academic materials shared within study groups. It supports file uploads (PDFs, notes, study guides), stores metadata for each resource, and allows group members to download or search for shared study materials.

### Chat Service
The Chat Service provides real-time messaging capabilities for group members. It manages message sending, message history storage, and retrieval of conversation threads for study group discussions.

### Scheduling Service
The Scheduling Service manages study session planning. Users can create study sessions, specify date and time, invite group members, and retrieve upcoming sessions linked to specific study groups.

### Notification Service
The Notification Service delivers system alerts to users. It sends notifications for events such as new messages, upcoming study sessions, new resource uploads, or group invitations.

### Search Service
The Search Service provides indexing and query functionality for the platform. It enables users to search for study groups, study materials, or potential study partners based on course names or keywords.