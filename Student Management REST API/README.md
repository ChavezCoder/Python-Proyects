# Student Management REST API

A lightweight Flask REST API that interacts with MySQL using `mysql-connector-python`.

## 📋 Prerequisites
Before running this project, ensure you have the following installed:
* **Python 3.8**
* **MySQL Server** (and administrative access via `root` or a dedicated user)
* **Git**

---

## 🖥️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_Student_API
   ```
2. ### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install Flask mysql-connector-python
```

### 4. Configure the database

Start MySQL and run the schema file from the repository root:

```bash
mysql -u root -p < schema.sql
```

This creates the `school_db` database and the following tables:

- `students`
- `courses`
- `enrollments`

Update the database credentials in `app.py` before starting the API:

```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'school_db'
}
```

Replace `your_password` with your MySQL password.

### 5. Start the API

From the repository root, run:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## 🔌 API Endpoints

### Get all students

```http
GET /students
```

### Create a student

```http
POST /students
Content-Type: application/json
```

Request body:

```json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "age": 36
}
```

### Update a student

```http
PUT /students/<student_id>
Content-Type: application/json
```

Request body:

```json
{
  "name": "Ada Byron Lovelace",
  "email": "ada.b@example.com",
  "age": 36
}
```

### Delete a student

```http
DELETE /students/<student_id>
```

Deleting a student also deletes their enrollments because the database uses `ON DELETE CASCADE`.

### Enroll a student in a course

```http
POST /enroll
Content-Type: application/json
```

Request body:

```json
{
  "student_id": 1,
  "course_id": 2
}
```

### Get a student's courses

```http
GET /students/<student_id>/courses
```

Example response:

```json
[
  {
    "id": 2,
    "title": "Introduction to Python",
    "code": "PY101"
  }
]
```

### Remove a student from a course

```http
DELETE /enroll
Content-Type: application/json
```

Request body:

```json
{
  "student_id": 1,
  "course_id": 2
}
```

## ✅ HTTP Status Codes

- `200 OK` — Request completed successfully
- `201 Created` — Student or enrollment created successfully
- `400 Bad Request` — Required data is missing or invalid
- `404 Not Found` — Student or enrollment does not exist

## ⚠️ Current Limitations

- Courses must currently be inserted into MySQL manually because there is no course-creation endpoint.
- Database credentials are stored directly in `app.py`; environment variables should be used in production.
- The database schema requires `age`, so the student create and update handlers must read and save that field.
- The student creation handler should call `conn.commit()` instead of `cursor.commit()`.
- The application currently runs with Flask debug mode enabled. Disable debug mode before deploying publicly.
