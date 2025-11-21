# friday-ai-web-app
# Friday AI Web App

This is a simple web application using Flask that serves as an OpenAI-powered FRIDAY assistant.

## Requirements

- Python 3.7+
- Flask
- OpenAI Python library
- OpenAI API key

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/aaronjoephilip01-oss/friday-ai-web-app.git
   cd friday-ai-web-app
   ```

2. Install the requirements:
   ```sh
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to `app.py`:
   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```

4. Run the application:
   ```sh
   python app.py
   ```

5. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Usage

- Enter any question in the box and press "Ask". FRIDAY will reply using OpenAI's GPT model.

## Customization

You can modify the HTML or Flask code to add features like voice, timers, authentication, or APIs.
