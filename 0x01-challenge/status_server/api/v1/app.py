from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
