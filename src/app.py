from flask import Flask, request, jsonify, send_from_directory
import os
import main

app = Flask(__name__)
FILES_DIR = 'files'

# Ensure the 'files' directory exists
if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

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

@app.route('/save-file', methods=['POST'])
def save_file():
    data = request.json
    text1 = data.get('text1')
    text2 = data.get('text2')
    text3 = data.get('text3')
    text4 = data.get('text4')
    text5 = data.get('text5')
    text6 = data.get('text6')

    # if not text1 or not text2 or not text3 or not text4 or not text5 or not text6:
    #     return jsonify({'error': 'Both text boxes must be filled out.'}), 400
    
    with open('data.txt', 'a') as file:
        file.write(f'{text1}, {text2}, {text3}, {text4}, {text5}, {text6}\n')
    return jsonify({'message': 'Data saved successfully'})

    
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


