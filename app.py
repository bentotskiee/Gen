from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
from translations import translate_genz_word, suggest_closest_word

app = Flask(__name__)

# Ensure 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Path to save the audio file
AUDIO_FILE_PATH = 'static/translation.mp3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        genz_word = data.get('word', '').strip()
        language = data.get('language', 'en')

        if not genz_word:
            return jsonify({"translation": "Input is empty", "audio_url": "", "suggestion": ""}), 400

    
        translation = translate_genz_word(genz_word, language)
        suggestion = ""

        
        if translation == "Translation not found.":
            suggestion = suggest_closest_word(genz_word)

        
        audio_url = ""
        if translation != "Translation not found.":
            
            tts_lang = 'tl' if language == 'tl' else 'en'
            tts = gTTS(text=translation, lang=tts_lang)

            
            tts.save(AUDIO_FILE_PATH)
            audio_url = f"{AUDIO_FILE_PATH}?t={os.path.getmtime(AUDIO_FILE_PATH)}"  # Prevent caching

        return jsonify({
            "translation": translation,
            "audio_url": audio_url,
            "suggestion": suggestion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
