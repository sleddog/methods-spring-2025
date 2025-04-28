from flask import Flask, request, jsonify

app = Flask(__name__)

def bobcat_fizzbuzz(n):
        """
    Generates the "BobCat FizzBuzz" sequence for numbers from 1 to n.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        list: A list of strings representing the "BobCat FizzBuzz" sequence.
              - "Bob" for multiples of 3.
              - "Cat" for multiples of 5.
              - "BobCat" for multiples of both 3 and 5.
              - The number itself as a string otherwise.
    """

    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("BobCat")
        elif i % 5 == 0:
            results.append("Cat")
        elif i % 3 == 0:
            results.append("Bob")
        else:
            results.append(str(i))
    return results

@app.route('/bobcat_fizzbuzz', methods=['GET'])
def fizzbuzz_endpoint():
    """
    API endpoint to generate the "BobCat FizzBuzz" sequence.

    Query Parameters:
        n (int): The upper limit of the sequence (must be an integer >= 1).

    Returns:
        JSON response:
            - 200 OK: A JSON object with the "results" key containing the sequence.
            - 400 Bad Request: A JSON object with an "error" key describing the issue.
    """
    
    n_param = request.args.get('n')
    if n_param is None:
        return jsonify(error="Missing required query parameter 'n'"), 400

    try:
        n = int(n_param)
    except ValueError:
        return jsonify(error="'n' must be an integer"), 400

    if n < 1:
        return jsonify(error="'n' must be >= 1"), 400

    output = bobcat_fizzbuzz(n)
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(debug=True)
