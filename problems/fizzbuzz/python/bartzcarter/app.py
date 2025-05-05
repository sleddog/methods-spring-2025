from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    number = request.form.get('number', type=int)
    result = generate_fizzbuzz(number)
    return render_template('result.html', number=number, result=result)

@app.route('/api/fizzbuzz', methods=['GET'])
def api_fizzbuzz():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({'error': 'Missing or invalid number parameter'}), 400
    result = generate_fizzbuzz(number)
    return jsonify({
        'input': number,
        'result': result
    })

def generate_fizzbuzz(number):
    result = []
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == '__main__':
    app.run(debug=True ,use_reloader=False)