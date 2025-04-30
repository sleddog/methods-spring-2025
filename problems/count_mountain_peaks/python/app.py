# app.py
from flask import Flask, request, jsonify
from script import count_mountain_peaks

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    input_array = data.get('input')
    if not isinstance(input_array, list):
        return jsonify({"error": "Input must be a list of numbers"}), 400

    result = count_mountain_peaks(input_array)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

