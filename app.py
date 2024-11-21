from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from waitress import serve  # Import Waitress

app = Flask(__name__)
CORS(app)

data = pd.read_excel("./BACKEND/VOTE.xlsx")

@app.route("/get-data", methods=["POST"])
def get_data():
    user_input = request.json.get('query', '').strip()
    data['HRMS'] = data['HRMS'].astype(str)
    data['IPAS'] = data['IPAS'].astype(str)
    if user_input.isdigit():
        result = data[data['HRMS'] == user_input]
    else:
        result = data[data['IPAS'] == user_input]
    if result.empty:
        return jsonify({"message": "No data found"}), 200
    return jsonify(result.to_dict(orient='records')), 200

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)  # Use Waitress to serve
