from flask import Flask
from datetime import datetime
from asgiref.wsgi import WsgiToAsgi

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page that returns "Hello [with today's date]"
@app.route('/')
def home():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"Hello from Tomi, today's date is {today}. <br>This is first deployment using flask"

# Wrap the Flask app to make it ASGI-compatible
asgi_app = WsgiToAsgi(app)

# Run the application (via uvicorn)
if __name__ == '__main__':
    app.run(debug=True)

