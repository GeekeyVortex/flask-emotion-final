from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector  # Assuming emotion_detector is your function

# Initialize Flask app
app = Flask(__name__,
            template_folder='oaqjp-final-project-emb-ai/templates',  # Path to the templates folder
            static_folder='oaqjp-final-project-emb-ai/static')  # Path to the static folder

# Route for serving the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for emotion detection
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    statement = request.json.get('statement')
    if statement:
        emotions = emotion_detector(statement)
        return jsonify(emotions)
    return jsonify({"error": "No statement provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
