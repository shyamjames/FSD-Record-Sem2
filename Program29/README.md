# Silvia.AI (formerly AI Web Assistant)

**Silvia.AI** is a futuristic, AI-powered web assistant and a dedicated Python library for AI interaction.

![Silvia.AI Home](https://github.com/shyamjames/AI-Web-Helper/blob/main/img/silvia.png?raw=true)

## Features

*   **AI Chat**: Powered by Google Gemini (via `ai_web_helper` library).
*   **Text Summarization**: Instantly summarize long blocks of text.
*   **Persistent History**: Chat sessions are saved.
*   **Secure**: API keys managed via `.env`.

## Project Structure

This repository contains two main components:

1.  **`ai_web_helper_pkg/`**: A reusable Python package that handles the AI logic (Gemini API interaction).
2.  **`flask_app/`**: The Flask web application that provides the Silvia.AI interface.

## Installation & Usage

### Prerequisites
*   Python 3.8+
*   Google Gemini API Key

### 1. Setup
Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/shyamjames/AI-Web-Helper.git
cd AI-Web-Helper
python3 -m venv venv
source venv/bin/activate
```

### 2. Install the Library
Install the custom AI helper package:
```bash
pip install -e ai_web_helper_pkg/
```
*Note: You also need to install Flask and other dependencies if not already installed.*
```bash
pip install flask python-dotenv google-generativeai markdown
```

### 3. Configure API Key
Create a `.env` file in the `flask_app` directory:
```bash
cd flask_app
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### 4. Run the Application
Start the Silvia.AI server:
```bash
python3 app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## License
[MIT License](LICENSE)
