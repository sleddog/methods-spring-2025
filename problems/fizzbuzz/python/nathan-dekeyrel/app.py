from flask import Flask, jsonify, request
from main import fizzbuzz
import io
import sys

app = Flask(__name__)

@app.route("/fizzbuzz", methods=['GET'])
def get_fizzbuzz():
    number = request.args.get('number', default=15, type=int)
    
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    fizzbuzz(number)
    
    output = new_stdout.getvalue().strip().split('\n')
    sys.stdout = old_stdout
    
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
