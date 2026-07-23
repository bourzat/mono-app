import os
import requests
from dotenv import load_dotenv

# Load credentials securely from .env
load_dotenv()

# Grab the refresh token from .env
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")

def run_quick_test():
    # 1. Get fresh token
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }
    
    res = requests.post(auth_url, data=payload)
    if res.status_code != 200:
        print(f"Auth failed: {res.text}")
        return

    access_token = res.json().get("access_token")

    # 2. Fetch activities
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(activities_url, headers=headers)
    if response.status_code == 200:
        print(f"Fetched {len(response.json())} activities successfully!")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    run_quick_test()