from googletrans import Translator
from langdetect import detect
import os

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def save_to_file(input_text, translated_text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Input text: {input_text}\n")
        f.write(f"Translated text: {translated_text}\n")

if __name__ == "__main__":
    user_input = input("Enter the text you want to translate: ")

    # Detect the language of the input text
    detected_language = detect(user_input)

    print(f"Detected language: {detected_language}")

    # Translate to English (or any desired language)
    translated_text = translate_text(user_input, 'en')
    print(f"Translated text: {translated_text}")

    target_language = input("Enter the target language: ")

    # Translate to the target language
    translated_text = translate_text(translated_text, target_language)
    print(f"Translated text: {translated_text}")

    filename = f"{target_language}.txt"
    save_to_file(user_input, translated_text, filename)
    print("Translation saved to: ", filename)
