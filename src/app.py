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

@app.route('/templates/form.html')
def form():
    return send_from_directory('templates', 'form.html')

@app.route('/images/Virginia-Tech-Logo.png')
def VTimage():
    return send_from_directory('images', 'Virginia-Tech-Logo.png')

@app.route('/save-file', methods=['POST'])
def save_file():
    data = request.json
    text1 = data.get('text1')
    text2 = data.get('text2')

    print(main.getStr())

    if not text1 or not text2:
        return jsonify({'error': 'Both text boxes must be filled out.'}), 400

    file_content = f'Text Box 1: {text1}\nText Box 2: {text2}'
    file_path = os.path.join(FILES_DIR, 'output.txt')

    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
        return jsonify({'message': 'File saved successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


