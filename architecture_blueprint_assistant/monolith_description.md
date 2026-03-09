# Monolithic Architecture

The StudyConnect application follows a monolithic architecture where all backend logic is contained in a single application. All modules share the same codebase and communicate internally within the monolith.

## Components

- **Frontend Web/Mobile App**  
  The user interface where students, tutors, and administrators interact with the platform to access features such as study groups, chats, and resources.

- **Backend Monolith**  
  A single backend application that contains all business logic and manages communication between different modules.

- **Authentication Module**  
  Handles user registration, login, authentication, and session management.

- **User Profile Module**  
  Manages user information such as courses, profile data, and user preferences.

- **Study Group Management Module**  
  Allows users to create, join, and manage study groups for specific courses.

- **Resource Sharing Module**  
  Enables users to upload, download, and manage shared study materials like notes and documents.

- **Chat & Messaging Module**  
  Provides real-time communication between study group members.

- **Scheduling Module**  
  Allows users to create and manage study sessions using a calendar system.

- **Notification Module**  
  Sends alerts to users about study sessions, new messages, and uploaded resources.

- **Central Database**  
  Stores all application data including users, groups, messages, and study materials.