import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import pygame

def record_audio():
    """Record audio from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Original Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def translate_text(text, target_language):
    """Translate text into the target language."""
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        print(f"Translated Text ({target_language}): {translated.text}")
        return translated.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return None

def speak_text(text):
    """Convert text to speech and play it."""
    try:
        tts = gTTS(text=text, lang="en")
        tts.save("translated_audio.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("translated_audio.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Speech Error: {e}")

if __name__ == "__main__":
    target_language = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()
    recorded_text = record_audio()
    if recorded_text:
        translated_text = translate_text(recorded_text, target_language)
        if translated_text:
            speak_text(translated_text)
