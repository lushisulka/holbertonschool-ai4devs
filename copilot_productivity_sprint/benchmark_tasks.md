# Benchmark Tasks

## Task 1 - Create Place Endpoint
**Requirements**: Implement POST /places endpoint to add a new place with validation.  

**Inputs**:  
JSON body:  
{name: "Colosseum", latitude: 41.8902, longitude: 12.4922, category: "attraction"}  

**Outputs**:  
- Created place object with unique ID  

**Acceptance Criteria**:  
- Returns 201 on successful creation  
- Returns 400 if required fields are missing  
- Returns 400 if coordinates are invalid  

---

## Task 2 - Get Places with Pagination
**Requirements**: Implement GET /places endpoint with pagination.  

**Inputs**:  
Query parameters:  
- page (default: 1)  
- limit (default: 10)  

**Outputs**:  
- List of places  

**Acceptance Criteria**:  
- Returns 200 with list of places  
- Supports pagination using page and limit  
- Returns empty list if no data found  

---

## Task 3 - Add Review to Place
**Requirements**: Implement POST /places/{id}/reviews endpoint.  

**Inputs**:  
Path parameter: place ID  

JSON body:  
{rating: 5, comment: "Amazing place!"}  

**Outputs**:  
- Created review object  

**Acceptance Criteria**:  
- Returns 201 on success  
- Returns 404 if place not found  
- Returns 400 if rating is not between 1–5  

---

## Task 4 - Save Place to Favorites
**Requirements**: Implement POST /favorites endpoint to save a place for a user.  

**Inputs**:  
JSON body:  
{userId: "123", placeId: "456"}  

**Outputs**:  
- Confirmation message or saved object  

**Acceptance Criteria**:  
- Returns 200 on success  
- Returns 404 if place does not exist  
- Prevents duplicate favorites  

---

## Task 5 - Delete Place
**Requirements**: Implement DELETE /places/{id} endpoint.  

**Inputs**:  
Path parameter: place ID  

**Outputs**:  
- Confirmation message  

**Acceptance Criteria**:  
- Returns 204 on successful deletion  
- Returns 404 if place not found  
- Only authorized users can delete  