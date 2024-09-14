#testing
from flask import Flask, request, jsonify, send_from_directory, render_template_string
import sqlite3
import os
import main

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
def getData():
    data = request.json

    department = date.get("department")
    course_number = data.get("course_number")

    if not all([department, course_number]):
        return jsonify({'error': 'All fields must be filled out.'}), 400

    
    return jsonify({'error': department + course_number}), 500



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


    # if not text1 or not text2 or not text3 or not text4 or not text5 or not text6:
    #     return jsonify({'error': 'Both text boxes must be filled out.'}), 400
    
    with open('data.txt', 'a') as file:
        file.write(f'{text1}, {text2}, {text3}, {text4}, {text5}, {text6}\n')
    return jsonify({'message': 'Data saved successfully'})

@app.route('/templates/previousExam.html')
def home():
    # Read the contents of the text file
    with open('data.txt', 'r') as file:
        file_content = file.read()
    
    # Pass the content to the template
    return render_template_string('previousExam.html', file_content=file_content)

    
    # file_content = f'Text Box 1: {text1}\nText Box 2: {text2}'
    # file_path = os.path.join(FILES_DIR, 'output.txt')

    # try:
    #     with open(file_path, 'w') as file:
    #         file.write(file_content)
    #     return jsonify({'message': 'File saved successfully.'})
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
