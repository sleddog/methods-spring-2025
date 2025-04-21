from flask import Flask, request, redirect, render_template
from BobCat_FizzBuzz import fizzbuzz


app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    return redirect("/fizzbuzz")

@app.get('/fizzbuzz')
def fizzbuzz_input():
    return render_template("fizzbuzz_form.html")

@app.post('/fizzbuzz')
def fizzbuzz_output():
    input_value = request.form.get('fizzbuzz_input', None)
    try:
        number = int(input_value)
    except (ValueError, TypeError):
        return "Invalid input", 400
    output = fizzbuzz(number)
    return render_template("fizzbuzz_result.html", output=output)




if __name__ == '__main__':
    app.run(port=5000)