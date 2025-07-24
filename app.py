from flask import Flask, request, jsonify
from nb import Classifier  # Assuming your classifier code is in nb.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
clf = Classifier()
clf.retrain("train.csv")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    description = data.get("desc", "")
    prediction = clf.predict(description)
    return jsonify({"prediction": prediction})

#Test from terminal:
#curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"desc": ""}'

if __name__ == '__main__':
    app.run(debug=True)


