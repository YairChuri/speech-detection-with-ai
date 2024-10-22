from flask import Flask, request 
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_endpoint():
    data = request.json

    emotion = emotion_detector(data["text"])
    return emotion, 200


app.run(debug=True)