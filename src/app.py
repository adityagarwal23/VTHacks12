from flask import Flask, request, jsonify, send_from_directory, render_template_string
import sqlite3
import os

app = Flask(__name__)
FILES_DIR = 'files'

# Ensure the 'files' directory exists
if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

DATABASE = 'exams.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/templates/previousExam.html')
def previousExam():
    return send_from_directory('templates', 'previousExam.html')

@app.route('/templates/form.html')
def form():
    return send_from_directory('templates', 'form.html')

@app.route('/templates/feedback.html')
def feedback():
    return send_from_directory('templates', 'feedback.html')

@app.route('/images/Virginia-Tech-Logo.png')
def VTimage():
    return send_from_directory('images', 'Virginia-Tech-Logo.png')

@app.route('/get-data', methods=['POST'])
def get_data():
    data = request.json
    department = data.get('department')
    course_number = data.get('course_number')

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
    department = data.get('department')
    course_number = data.get('course_number')
    professor_last_name = data.get('professor_last_name')
    exam_difficulty = data.get('exam_difficulty')
    exam_score = data.get('exam_score')
    hours_spent_studying = data.get('hours_spent_studying')

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
