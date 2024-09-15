from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'exams.db'


def get_db():
    """
    get the database
    """
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    """gives the home page to the client

    Returns:
        html: the home screen html
    """    
    return send_from_directory('templates', 'index.html')

@app.route('/templates/previousExam.html')
def previousExam():
    """gives the html for the page to serch for previous exams to the client

    Returns:
        html: the html of the previousExam page
    """    
    return send_from_directory('templates', 'previousExam.html')

@app.route('/templates/form.html')
def form():
    """gives the html for the form to add an exam to the database

    Returns:
        html: the form as an html
    """    
    return send_from_directory('templates', 'form.html')

@app.route('/templates/feedback.html')
def feedback():
    """gives the contact us/feadbak page to the user

    Returns:
        html: the html page to contact us
    """    
    return send_from_directory('templates', 'feedback.html')

@app.route('/images/Virginia-Tech-Logo.png')
def VTimage():
    """gives the logo of our VT

    Returns:
        png: the image of the 
    """    
    return send_from_directory('images', 'Virginia-Tech-Logo.png')

@app.route('/get-data', methods=['POST'])
def get_data():
    data = request.json
    department = data.get('department').lower()
    course_number = data.get('course_number').lower()

    if not department or not course_number:
        return jsonify({'error': 'Department and course number are required.'}), 400

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT professor_last_name,
                   AVG(exam_difficulty) AS avg_exam_difficulty,
                   AVG(exam_score) AS avg_exam_score,
                   AVG(hours_spent_studying) AS avg_hours_spent_studying
            FROM exams
            WHERE department = ? AND course_number = ?
            GROUP BY professor_last_name
        ''', (department, course_number))

        rows = cursor.fetchall()
        conn.close()

        # Prepare results for the front end
        results = []
        for row in rows:
            results.append({
                'professor_last_name': row[0],
                'avg_exam_difficulty': row[1],
                'avg_exam_score': row[2],
                'avg_hours_spent_studying': row[3]
            })

        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-file', methods=['POST'])
def save_file():
    data = request.json
    department = data.get('department').lower()
    course_number = data.get('course_number').lower()
    professor_last_name = data.get('professor_last_name').capitalize()
    exam_difficulty = data.get('exam_difficulty').lower()
    exam_score = data.get('exam_score').lower()
    hours_spent_studying = data.get('hours_spent_studying').lower()

    if not all([department, course_number, professor_last_name, exam_difficulty, exam_score, hours_spent_studying]):
        return jsonify({'error': 'All fields must be filled out.'}), 400
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO exams (department, course_number, professor_last_name, exam_difficulty, exam_score, hours_spent_studying)
                       VALUES(?, ?, ?, ?, ?, ?)
                    ''', (department, course_number, professor_last_name, exam_difficulty, exam_score, hours_spent_studying))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Data saved successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
