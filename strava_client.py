import os
import requests
from dotenv import load_dotenv

# 1. Load variables from the .env file into Python's environment
load_dotenv()

CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")

def get_fresh_access_token():
    """
    Sends our refresh_token to Strava to obtain a brand new access_token.
    """
    url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }
    
    print("🔄 Requesting fresh access token from Strava...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        token_data = response.json()
        new_access_token = token_data.get("access_token")
        print("✅ Success! Obtained fresh access token.\n")
        return new_access_token
    else:
        print(f"❌ Failed to refresh token: {response.status_code}")
        print(response.text)
        return None

def fetch_latest_activity(access_token):
    """
    Fetches activities using the newly generated access_token.
    """
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        activities = response.json()
        print(f"Successfully fetched {len(activities)} activities!")
        if activities:
            latest = activities[0]
            print(f"Latest Activity: {latest.get('name')}")
            print(f"Distance: {latest.get('distance')} m")
    else:
        print(f"Error fetching activities: {response.status_code}")

# --- EXECUTION FLOW ---
if __name__ == "__main__":
    # Step A: Get a fresh access token programmatically
    token = get_fresh_access_token()
    
    # Step B: Use that token to fetch workout data
    if token:
        fetch_latest_activity(token)