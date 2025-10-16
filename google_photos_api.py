# import pickle
# import os.path
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build

# class API:
#     """Contains code to connct to and pull an album from google photos.
#     """
#     def __init__(self, key):
#         """Saves the API key as a class attribute.
#         """
#         self.key = key
#         self.scopes = ['https://www.googleapis.com/auth/photoslibrary.sharing']

#     def connect(self):
#         """Authenticates and returns a Google Photos API service object.
#         """
#         creds = None
#         if os.path.exists('token.pickle'):
#             with open('token.pickle', 'rb') as token:
#                 creds = pickle.load(token)

#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 # Delete old token if scopes have changed
#                 if os.path.exists('token.pickle'):
#                     os.remove('token.pickle')
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     'client_secrets.json', SCOPES)
#                 creds = flow.run_local_server(port=0)

#             with open('token.pickle', 'wb') as token:
#                 pickle.dump(creds, token)

#         service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
#         self.service = service
#         return service
    
#     def list_shared_albums(self):
#         """Gets a list of all shared albums in the user account.
#         """

#         results = service.sharedAlbums().list(pageSize=50).execute()
#         albums = results.get('sharedAlbums', [])
#         self.albums = albums
#         return albums
    
#     def get_album_by_name(self, album_name:str):
#         """Gets a specific album which has a specified name.
#         """
#         specified_album = None
#         for album in self.albums:
#             if album['title'] == album_name:
#                 specified_album = album
#                 break
#         return specified_album
    
#     def get_photos(self, album):
#         """Gets all photos from the album and returns them in a list.
#         """
#         photos = []
#         request_body = {
#             'albumId': album['id'],
#             'pageSize': 100
#         }



    

    
        
    





# def list_shared_albums(service):
#     """Lists all shared albums the app can access."""
#     # ✅ Use sharedAlbums().list() instead of albums().list()
#     results = service.sharedAlbums().list(pageSize=50).execute()
#     albums = results.get('sharedAlbums', [])

#     if not albums:
#         print('No shared albums found.')
#         print('Please make sure you have created a shareable link for your album in Google Photos.')
#     else:
#         print('Shared Albums:')
#         for album in albums:
#             # Note: Shared albums have 'title' and 'id' just like regular albums
#             print(f"- {album['title']} (ID: {album['id']})")
#     return albums

# def get_album_by_title(self, service, album_title):
#     """Finds a shared album by its title."""
#     results = service.sharedAlbums().list(pageSize=50).execute()
#     albums = results.get('sharedAlbums', [])
#     for album in albums:
#         if 'title' in album and album['title'] == album_title:
#             return album
#     return None

# def get_photos(self, album):


# def list_media_in_album(service, album_id):
#     """Lists all media items within a specific album."""
#     print(f"\nListing media in album (ID: {album_id})...")
#     request_body = {
#         'albumId': album_id,
#         'pageSize': 100
#     }
#     results = service.mediaItems().search(body=request_body).execute()
#     media_items = results.get('mediaItems', [])

#     if not media_items:
#         print("No media items found in this album.")
#     else:
#         for item in media_items:
#             print(f"- Filename: {item['filename']} (ID: {item['id']})")

# if __name__ == '__main__':
#     service = get_photos_service()
    
#     # List all shared albums your app can access
#     list_shared_albums(service)
    
#     # --- Example: Access a specific shared album ---
#     album_name_to_find = "Summer Trip"  # <-- CHANGE THIS to the name of your SHARED album
    
#     album = get_album_by_title(service, album_name_to_find)
    
#     if album:
#         list_media_in_album(service, album['id'])
#     else:
#         print(f"\nShared album '{album_name_to_find}' not found.")
    
    
