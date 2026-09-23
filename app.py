from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'school_db'
}

# Connecting to the database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# 1. Get ALL students
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students), 200

# 2. CREATE STUDENT
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    cursor.commit()

    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'id': new_id, 'name': name, 'email': email}), 201

# 3. Enroll STUDENT in a course (JOIN RELATIONSHIP)
@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if not student_id or not course_id:
        return jsonify({'error': 'Student ID and Course ID are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
    try:
        cursor.execute(query, (student_id, course_id))
        conn.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Student enrolled successfully"}), 201

# 4. GET ALL COURSES FOR A SPECIFIC STUDENT
@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT c.id, c.title, c.code
    FROM courses c
    JOIN enrollments e ON c.id = e.course_id
    WHERE e.student_id = %s
    """
    cursor.execute(query, (student_id,))
    courses = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(courses), 200

# 5. UPDATE A STUDENT (PUT)
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE students SET name = %s, email = %s WHERE id = %s"
    cursor.execute(query, (name, email, student_id))
    conn.commit()

    # Check if any row was actually modified
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    cursor.close()
    conn.close()
    return jsonify({"id": student_id, "name": name, "email": email}), 200

# 6. DELETE A STUDENT (DELETE)
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Due to ON DELETE CASCADE, deleting a student will also delete their enrollments
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    cursor.close()
    conn.close()
    return jsonify({"message": f"Student with ID {student_id} deleted successfully"}), 200

# 7. UNEROLL A STUDENT FROM A COURSE
@app.route('/enroll', methods=['DELETE'])
def unenroll_student():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if not student_id or not course_id:
        return jsonify({"error": "student_id and course_id are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM enrollments WHERE student_id = %s AND course_id = %s"
    cursor.execute(query, (student_id, course_id))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Enrollment not found"}), 404

    cursor.close()
    conn.close()
    return jsonify({"message": "Student succesfully unenrolled"}), 200

if __name__ == '__main__':
    app.run(debug=True)


