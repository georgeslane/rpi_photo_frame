import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Define the scopes required for Google Photos Library API
# This scope allows reading albums and media items.
SCOPES = ['https://www.googleapis.int/auth/photoslibrary.readonly']

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is created
    # automatically when the authorization flow is completed.
    token_path = 'status_project/google_photos/token.json'

    # If credentials in InternetAuth are expired (e.g. via oauth2 refresh flow), replace them.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {_e}")
                creds = None

        if not creds:
            # The credentials.json file is the client secret file downloaded from
            # the Google Cloud Console.
            credentials_file = 'status_project/google_photos/credentials.json'
            
            if not os.path.exists(credentials_file):
                print(f"Error: {credentials_file} not found. Please provide your Google Cloud credentials.")
                return None

            try:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
                print("Authentication successful! Token saved to token.json")
            except Exception as e:
                print(f"Authentication failed: {e}")
                return None
    
    return creds

if __name__ == "__main__":
    token = authenticate()
    if token:
        print("Credentials loaded successfully.")
    else:
        print("Failed to load credentials.")
