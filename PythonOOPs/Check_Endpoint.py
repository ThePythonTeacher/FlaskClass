import requests
import time

# API headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer rpa_NS38SU5DW8E26KEEIY3G75YHGM11ND4RG2RDWR7Lb8yt76'
}

# Data to send
data = {
    'input': {
        "prompt": "sample python code for hellow world ",
        "max_tokens": 3000  # Set max tokens here
    }
}
# Send request
response = requests.post('https://api.runpod.ai/v2/wlmc59x5arw72s/run', headers=headers, json=data)
response_json = response.json()

# Extract job ID
job_id = response_json.get("id")
if not job_id:
    print("Error: No job ID returned.")
    exit()

# Polling the status endpoint
status_url = f"https://api.runpod.ai/v2/wlmc59x5arw72s/status/{job_id}"

while True:
    status_response = requests.get(status_url, headers=headers)
    status_json = status_response.json()

    if status_json.get("status") == "COMPLETED":
        print("Result:", status_json.get("output"))
        break
    elif status_json.get("status") == "FAILED":
        print("Error: Job failed.")
        break

    print("Waiting for result...")
    time.sleep(2)  # Wait before retrying



