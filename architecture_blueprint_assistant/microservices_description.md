# Microservices Architecture

The StudyConnect system is decomposed into independent microservices. Each service manages a specific function and maintains its own database. Communication between services happens through the API Gateway.

## Services

- **API Gateway**
  The central entry point for all client requests. It routes requests to the correct microservice and handles authentication and request management.

- **Auth Service**
  Handles user authentication including registration, login, token generation, and access control.

- **User Service**
  Manages user profile data such as personal information, enrolled courses, and preferences.

- **Study Group Service**
  Responsible for creating, joining, and managing study groups and their members.

- **Resource Service**
  Handles uploading, storing, and downloading study materials such as notes and documents.

- **Chat Service**
  Provides messaging functionality between users and within study groups.

- **Scheduling Service**
  Manages study session scheduling, including creating sessions and storing time and participant information.

- **Notification Service**
  Sends alerts and updates to users about messages, resources, or scheduled study sessions.

- **Search Service**
  Enables searching for study groups, study materials, and matching students based on courses.