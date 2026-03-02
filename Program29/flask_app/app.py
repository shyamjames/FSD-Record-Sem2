from flask import Flask, render_template, request, session, redirect, url_for
from ai_web_helper import get_response, summarize_text, format_response
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super_secret_key_for_dev") # Needed for session

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "")

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        action = request.form.get('action')
        
        if user_input:
            if not API_KEY:
                response_text = "Error: API Key is missing. Please set GEMINI_API_KEY environment variable."
                session['history'].append({'role': 'user', 'content': user_input})
                session['history'].append({'role': 'ai', 'content': response_text})
            else:
                # Add user message to history
                session['history'].append({'role': 'user', 'content': user_input})
                
                if action == 'summarize':
                    raw_response = summarize_text(user_input, API_KEY)
                else:
                    raw_response = get_response(user_input, API_KEY)
                
                response_text = format_response(raw_response)
                
                # Add AI response to history
                session['history'].append({'role': 'ai', 'content': response_text})
            
            session.modified = True
            return redirect(url_for('index'))
    
    return render_template('index.html', history=session.get('history', []))

@app.route('/clear', methods=['POST'])
def clear_history():
    session.pop('history', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
