"""
app.py - A Flask web API that returns snow conditions based on temperature
Run with: python app.py
Access endpoint at: http://127.0.0.1:5000/snow_condition?temp=25
"""

from flask import Flask, request, jsonify
from main import snow_conditions

app = Flask(__name__)


@app.route('/snow_condition', methods=['GET'])
def get_snow_condition():
    temp = request.args.get('temp', type=int)
    if temp is None:
        return jsonify({"error": "Please provide a temperature as a query parameter (e.g., ?temp=25)"}), 400
    condition = snow_conditions(temp)
    return jsonify({"temperature": temp, "condition": condition})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
