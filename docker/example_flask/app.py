import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/can-i-golf')
def can_i_golf():
    if determine_golf_ability():
        return 'Yes'
    else:
        return 'No'


def determine_golf_ability():
    # if the current time is between 6am and 8pm return True
    # else return False
    current_hour = time.time()
    if 6 <= current_hour <= 20:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
