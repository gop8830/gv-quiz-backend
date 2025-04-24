
from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF

app = Flask(__name__)
CORS(app)

@app.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    file = request.files.get('pdf')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = "\n".join(page.get_text() for page in doc)

        questions = [
            {
                "question": "What is one key hazard mentioned in the document?",
                "options": ["Slips", "Electrical Shock", "Noise", "Poor Lighting"],
                "answer": 1
            },
            {
                "question": "Which class of fire involves electrical equipment?",
                "options": ["Class A", "Class B", "Class C", "Class D"],
                "answer": 2
            }
        ]

        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
