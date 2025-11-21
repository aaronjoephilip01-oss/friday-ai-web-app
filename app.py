from flask import Flask, render_template_string, request
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Put your OpenAI key here!

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>FRIDAY AI Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #0084ff; }
        .response { margin-top: 20px; font-size: 1.2em; color: #333; }
        input[type=text] { width: 400px; padding: 10px; }
        input[type=submit] { padding: 10px 20px; background: #0084ff; color: white; border: none; }
    </style>
</head>
<body>
    <h1>FRIDAY AI Assistant</h1>
    <form method="post">
        <input type="text" name="question" placeholder="Ask FRIDAY anything..." required />
        <input type="submit" value="Ask" />
    </form>
    <div class="response">
        {% if response %}
            <strong>FRIDAY:</strong> {{ response }}
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    friday_response = ""
    if request.method == "POST":
        question = request.form.get("question", "")
        if question:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            friday_response = response.choices[0].message["content"]
    return render_template_string(html, response=friday_response)

if __name__ == "__main__":
    app.run(debug=True)