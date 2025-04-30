# Count Mountain Peaks API

How to Run
1. Install Flask - (pip install flask)
2. Run the app - (python mountain_peaks_api.py)
3. The server will start at http://127.0.0.1:5000

To use the API

Send a POST request to the /count_peaks endpoint with a JSON payload containing a list of elevation values.

Example Curl Request!

curl -X POST http://127.0.0.1:5000/count_peaks \
     -H "Content-Type: application/json" \
     -d '{"elevations": [4500, 7200, 6800, 8100, 7900, 9000, 8500]}'

Expected Response
{"You have this many peaks!": 3}
