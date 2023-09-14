# Flask REST API Documentation

This document provides detailed information on the usage and setup of the Flask REST API for managing person records.

## Endpoints

### Create Person

- **Endpoint**: `POST /api`
- **Request Format**: JSON
  - Example Request Body:
    ```json
    {
      "name": "John Doe"
    }
    ```
- **Response Format**: JSON
  - Example Response (Success):
    ```json
    {
      "message": "Person created successfully",
      "person_id": 1
    }
    ```
  - Example Response (Error):
    ```json
    {
      "error": "Name is required"
    }
    ```

### Get Person

- **Endpoint**: `GET /api/{person_id}`
- **Response Format**: JSON
  - Example Response (Success):
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
  - Example Response (Error):
    ```json
    {
      "error": "Person not found"
    }
    ```

### Update Person

- **Endpoint**: `PUT/PATCH /api/{person_id}`
- **Request Format**: JSON
  - Example Request Body:
    ```json
    {
      "name": "Updated Name"
    }
    ```
- **Response Format**: JSON
  - Example Response (Success):
    ```json
    {
      "message": "Person updated successfully",
      "person_id": 1
    }
    ```
  - Example Response (Error):
    ```json
    {
      "error": "Person not found"
    }
    ```

### Delete Person

- **Endpoint**: `DELETE /api/{person_id}`
- **Response Format**: JSON
  - Example Response (Success):
    ```json
    {
      "message": "Person deleted successfully"
    }
    ```
  - Example Response (Error):
    ```json
    {
      "error": "Person not found"
    }
    ```

## Sample Usage

- **Create a Person:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8080/api

  Get Person Details:

bash
Copy code
curl http://localhost:8080/api/1
Update Person's Name:

bash
Copy code
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:8080/api/1
Delete a Person:

bash
Copy code
curl -X DELETE http://localhost:8080/api/1
Limitations and Assumptions
The API assumes that person records are identified by unique integer IDs.
Only the name attribute is required for creating and updating a person record.
Setup and Deployment
Clone the repository.
Install dependencies: pip install -r requirements.txt.
Create the SQLite database: python app.py.
Start the Flask application: python app.py.
The API will be available at http://localhost:8080.
