from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        english_text = request.form['text']
        if not english_text.strip():
            return jsonify({'error': 'Please enter some text to translate'})
        
        translation = GoogleTranslator(source='en', target='hi').translate(english_text)
        return jsonify({
            'english': english_text,
            'hindi': translation
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)