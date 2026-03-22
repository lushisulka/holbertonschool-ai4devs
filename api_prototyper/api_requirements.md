# API Requirements – Travel Map Discovery App

## Domain
Travel discovery platform providing city maps, points of interest, reviews, and travel guides.

## Target Users
- Travelers: fetch places, view details, save favorites  
- Locals: add new places, write reviews  
- Content Creators: create and share travel guides  
- Mobile/Web developers: integrate app with backend services  

## Core Operations
- Get list of cities  
- Get points of interest by city  
- Get details for a specific place  
- Add new place  
- Update place information  
- Delete place (admin only)  
- Add review for a place  
- Get reviews for a place  
- Create travel guide  
- Get travel guides by city  
- Update travel guide  
- Save/unsave place to user favorites  

## Data Validation Rules
- Place name: required, max 100 characters  
- Coordinates (lat, long): must be valid decimal numbers  
- Rating: 1–5  
- User email: valid email format  
- Guide title: required, max 100 characters  
- Review text: max 500 characters  

## Non-Functional Requirements
- Response time < 300ms for read operations  
- JWT authentication for all user-specific actions  
- Admin endpoints require role-based access control  
- Rate limit: 100 requests per minute per user  
- HTTPS required for all endpoints  
- Logging for all write operations  