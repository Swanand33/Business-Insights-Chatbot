import requests
import json

url = "http://127.0.0.1:5000/chat"  # Ensure it matches Flask app
payload = {"message": "Provide financial insights for tech startups."}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.ConnectionError:
    print("❌ ERROR: Unable to connect to Flask server. Ensure `app.py` is running.")