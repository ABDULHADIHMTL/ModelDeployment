import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Your route definitions here
@app.route('/')
def home():
    return "Welcome to the ML Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Your prediction logic here
    prediction = 0  # Replace with actual prediction logic
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

