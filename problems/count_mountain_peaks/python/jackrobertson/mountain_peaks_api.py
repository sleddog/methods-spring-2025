from flask import Flask, request, jsonify

app = Flask(__name__)

def count_mountain_peaks(elevations):
    peaks = 0
    for i in range(1, len(elevations) - 1):
        if elevations[i] > elevations[i - 1] and elevations[i] > elevations[i + 1]:
            peaks += 1
    return peaks

@app.route('/count_peaks', methods=['POST'])
def count_peaks():
    elevations = request.get_json().get('elevations', [])
    return jsonify({'You have this many peaks!': count_mountain_peaks(elevations)})

if __name__ == '__main__':
    app.run()
