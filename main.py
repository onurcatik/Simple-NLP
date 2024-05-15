import speech_recognition as sr
import spacy

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    """
    Process the transcribed text using Spacy.
    
    Args:
    text (str): The transcribed text.
    
    Returns:
    None
    """
    doc = nlp(text)
    for token in doc:
        print(token.text, token.pos_)

def transcribe_speech():
    """
    Transcribe speech input from the microphone.
    
    Returns:
    str: Transcribed text, or None if speech recognition fails.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)  # Listen for speech input

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def main():
    """
    Main function to transcribe and process speech input.
    """
    while True:
        spoken_text = transcribe_speech()

        if spoken_text:
            process_text(spoken_text)

if __name__ == "__main__":
    main()
