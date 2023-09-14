# Flask REST API for Managing Persons

A simple Flask-based REST API for CRUD operations on person records.

## Usage

- **Create Person:** `POST /api` with JSON data `{"name": "John Doe"}`.
- **Get Person:** `GET /api/{person_id}`.
- **Update Person:** `PUT/PATCH /api/{person_id}` with JSON data `{"name": "Updated Name"}`.
- **Delete Person:** `DELETE /api/{person_id}`.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create the SQLite database: `python app.py`.
4. Start the Flask application: `python app.py`.

The API will be available at `http://localhost:8080`.

## Sample Usage

- Create a person:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8080/api

tests - postman



