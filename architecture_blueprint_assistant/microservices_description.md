# Microservices Architecture

In the microservices architecture, the StudyConnect application is divided into multiple independent services. Each service handles a specific responsibility and has its own database. Services communicate through APIs managed by the API Gateway.

## Services

- **API Gateway**  
  Acts as the single entry point for all client requests. It routes requests to the appropriate microservice and handles security, rate limiting, and request validation.

- **Auth Service**  
  Manages user authentication and authorization including login, registration, and token validation.

- **User Profile Service**  
  Handles user profile data such as personal information, enrolled courses, and preferences.

- **Study Group Service**  
  Responsible for creating, joining, and managing study groups and group memberships.

- **Resource Service**  
  Manages uploading, storing, and retrieving shared study materials such as notes and documents.

- **Chat Service**  
  Enables messaging between users within study groups and manages chat history.

- **Scheduling Service**  
  Allows users to create and manage study sessions, including date, time, and participant information.

- **Notification Service**  
  Sends notifications to users about events such as new messages, scheduled sessions, or uploaded resources.

- **Search & Matching Service**  
  Provides functionality for searching study resources and matching students with study partners based on courses or interests.