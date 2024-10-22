import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    data = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        strongest_emotion = ""
        strongest_emotion_score = 0
        for emotion, score in result["emotionPredictions"][0]["emotion"].items():
            if score > strongest_emotion_score:
                strongest_emotion = emotion
                strongest_emotion_score = score
        print("Strongest Emotion: " + strongest_emotion)
        formatted_json = json.dumps(result, indent=4)
        print(formatted_json)
    else:
        print(f'Error: {response.status_code}, {response.text}')

text = "I love this new technology."
emotion_detector(text)