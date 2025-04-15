from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # return the contents from local file
    return open('numbers.html').read()

# expose a /numbers route that pull the upper number from the form post parameters
@app.route('/numbers', methods=['POST'])
def numbers_post():
    # pull the upper number from the form post parameters
    n = int(request.form.get('number'))
    return ' '.join(numbers(n))

def numbers(n):
    return [str(i) for i in range(1, n + 1)]

if __name__ == '__main__':
    app.run()
