import pytest
from EmotionDetection import emotion_detector

def test_joy():
    emotions = emotion_detector("I am glad this happened")
    assert emotions["dominant_emotion"] == "joy"

def test_anger():
    emotions = emotion_detector("I am really mad about this")
    assert emotions["dominant_emotion"] == "anger"

def test_disgust():
    emotions = emotion_detector("I feel disgusted just hearing about this")
    assert emotions["dominant_emotion"] == "disgust"

def test_sadness():
    emotions = emotion_detector("I am so sad about this")
    assert emotions["dominant_emotion"] == "sadness"

def test_fear():
    emotions = emotion_detector("I am really afraid that this will happen")
    assert emotions["dominant_emotion"] == "fear"
