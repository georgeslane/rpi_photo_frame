import os
import time
import requests
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Configuration
SCOPES = ['https://www.googleapis.int/auth/photoslibrary.readonly']
TOKEN_PATH = 'status_project/google_photos/token.json'
PHOTO_DIR = os.path.expanduser("~/photos_frame")

def get_service():
    if not os.path.exists(TOKEN_PATH):
        print("Error: token.json not found. Please run auth_helper.py first.")
        return None
    
    creds = Credentials.from_authorized__user_file(TOKEN_PATH, SCOPES)
    service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
    return service

def sync_photos(album_id=None):
    service = get_service()
    if not service:
        return

    if not os.path.exists(PHOTO_DIR):
        os.makedirs(PHOTO_DIR)

    try:
        # If album_id is provided, search within that album. Otherwise, list all media items.
        if album_id:
            search_body = {"albumId": album_id, "pageSize": 50}
            results = service.mediaItems().search(body=search_body).execute()
        else:
            results = service.mediaItems().list(pageSize=50).execute()

        items = results.get('mediaItems', [])
        
        if not items:
            print("No photos found to sync.")
            return

        for item in items:
            filename = item['filename']
            # We use the baseUrl to get the actual image. 
            # Note: baseUrl is a temporary link to the image.
            image_url = item['baseUrl'] + "=d" # '=d' tells Google to provide the high-res version
            
            target_path = os.path.join(PHOTO_DIR, filename)
            
            if os.path.exists(target_path):
                print(f"Skipping {filename} (already exists)")
                continue

            print(f"Downloading {filename}...")
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(target_path, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded {filename}")
            else:
                print(f"Failed to download {filename}: Status {response.status_code}")

        print("Sync completed successfully.")

    except Exception as e:
        print(f"Error during sync: {e}")

if __name__ == "__main__":
    sync_photos()
