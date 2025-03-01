from flask import Flask, request, jsonify
import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Get database URL from environment variable
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/studentsdb')
logger.info(f"Connecting to database: {DATABASE_URL}")

# Wait for the database to be ready
max_retries = 30
for i in range(max_retries):
    try:
        logger.info(f"Attempt {i+1}/{max_retries} to connect to the database...")
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        logger.info("Successfully connected to the database!")
        break
    except Exception as e:
        if i == max_retries - 1:
            logger.error(f"Failed to connect to the database after {max_retries} attempts: {e}")
            raise e
        time.sleep(1)
        logger.warning(f"Retry connecting to the database ({i+1}/{max_retries})...")

# Define database model
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=True)
    edad = Column(Integer, nullable=True)
    carrera = Column(String(100), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'carrera': self.carrera
        }

# Create the database tables
logger.info("Creating database tables if they don't exist...")
Base.metadata.create_all(engine)
logger.info("Database tables created or already exist")

# Create a session factory
Session = sessionmaker(bind=engine)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Student API is running",
        "endpoints": {
            "GET /students": "Get all students",
            "GET /students/<id>": "Get a specific student",
            "POST /students": "Create a new student",
            "PUT /students/<id>": "Update a student",
            "DELETE /students/<id>": "Delete a student"
        }
    })

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    session = Session()
    try:
        students = session.query(Student).all()
        return jsonify([student.to_dict() for student in students])
    except Exception as e:
        logger.error(f"Error retrieving students: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# Route to get a specific student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    session = Session()
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            return jsonify(student.to_dict())
        return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        logger.error(f"Error retrieving student {student_id}: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    session = Session()
    data = request.json
    logger.info(f"Received request to add student: {data}")
    
    try:
        # Validate required fields
        if 'nombre' not in data:
            return jsonify({"error": "Field 'nombre' is required"}), 400
            
        # Create a new student with provided fields
        student_data = {}
        for field in ['nombre', 'edad', 'carrera']:
            if field in data:
                student_data[field] = data[field]
                
        new_student = Student(**student_data)
        session.add(new_student)
        session.commit()
        logger.info(f"Added new student with ID: {new_student.id}")
        
        return jsonify(new_student.to_dict()), 201
    except Exception as e:
        session.rollback()
        logger.error(f"Error adding student: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# Route to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    session = Session()
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
            
        session.delete(student)
        session.commit()
        logger.info(f"Deleted student with ID: {student_id}")
        
        return jsonify({"message": f"Student {student_id} deleted successfully"}), 200
    except Exception as e:
        session.rollback()
        logger.error(f"Error deleting student {student_id}: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# Route to update a student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    session = Session()
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
            
        data = request.json
        logger.info(f"Updating student {student_id} with data: {data}")
        
        # Update fields that are provided
        for field in ['nombre', 'edad', 'carrera']:
            if field in data:
                setattr(student, field, data[field])
                
        session.commit()
        logger.info(f"Updated student with ID: {student_id}")
        
        return jsonify(student.to_dict()), 200
    except Exception as e:
        session.rollback()
        logger.error(f"Error updating student {student_id}: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)
