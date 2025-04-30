from flask import Flask, request, jsonify

app = Flask(__name__)

def bobcatbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append("BobCat")
        elif i % 5 == 0:
            result.append("Cat")
        elif i % 3 == 0:
            result.append("Bob")
        else:
            result.append(i)
    return result

@app.route('/api/bobcatbuzz', methods=['GET','POST'])
def bobcatbuzzapi():
    if request.method == "POST":
        data = request.get_json()
        n = data.get('n')
    else:
        n = request.args.get('n', type=int)

    if not isinstance(n, int) or n < 1:
        return jsonify({'status': 'error', 'message': 'n must be an integer'})

    output = bobcatbuzz(n)
    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run()
