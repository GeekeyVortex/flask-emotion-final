"""
server.py
Flask-based web server for an emotion detection application using Watson NLP API.
"""


from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector  # Assuming emotion_detector is your function

# Initialize Flask app
app = Flask(__name__,
            template_folder='oaqjp-final-project-emb-ai/templates',  # Path to the templates folder
            static_folder='oaqjp-final-project-emb-ai/static')  # Path to the static folder

# Route for serving the index page
@app.route('/')
def index():
    """
    Renders the main index page of the web application.
    """
    return render_template('index.html')

# Route for emotion detection
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():

    """
    Handles POST requests for emotion detection.

    Returns:
        JSON response containing emotion analysis results or an error message.
    """
    statement = request.json.get('statement')
    if statement:
        emotions = emotion_detector(statement)
        # Handle the case where dominant_emotion is None
        if emotions['dominant_emotion'] is None:
            return jsonify({"error": "Invalid text! Please try again."}), 400
        return jsonify(emotions)
    return jsonify({"error": "No statement provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
