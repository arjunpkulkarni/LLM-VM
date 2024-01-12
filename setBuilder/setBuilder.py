# import our client
from llm_vm.client import Client
import os

import os
import requests  # To make HTTP requests

# Set your SoundCloud client_id, client_secret, and redirect_uri
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'

# Step 1: Redirect user to SoundCloud for authorization
auth_url = f"https://api.soundcloud.com/connect?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
# Redirect your user to this URL

# Step 2: User approves and you receive the code
# The code will be part of the query parameters in the redirect_uri

# Step 3: Exchange code for access token
def get_access_token(code):
    token_url = "https://api.soundcloud.com/oauth2/token"
    payload = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return response.json()  # This contains access_token and refresh_token
    else:
        return None

# Example usage
code = 'CODE_RECEIVED_FROM_REDIRECT'  # Replace with actual code
token_info = get_access_token(code)
if token_info:
    access_token = token_info['access_token']
    refresh_token = token_info['refresh_token']
    # Store these tokens securely

# Step 4: Refreshing the token (when needed)
def refresh_access_token(refresh_token):
    token_url = "https://api.soundcloud.com/oauth2/token"
    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return response.json()  # This contains the new access_token and refresh_token
    else:
        return None

# Example usage for refreshing the token
new_token_info = refresh_access_token(refresh_token)
if new_token_info:
    access_token = new_token_info['access_token']
    refresh_token = new_token_info['refresh_token']
    # Update your stored tokens


# Instantiate the client specifying which LLM you want to use
client = Client(big_model='chat_gpt', small_model='gpt') #REBEL will use chat_gpt no matter what big model is specified here, this specification exists for non-REBEL completion calls. 
response = client.complete(
    prompt='You are an AI meant to give me DJ sets specified to the artist I want and the mood I want. Ask that first no matter what I ask for. That should be what you come in with.',
    context='',
    openai_key=os.getenv("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"),  # Replace with your actual OpenAI key
    tools=[
        {
            'description': 'Create a SoundCloud playlist',
            'dynamic_params': {
                "title": "Title of the playlist",
                "description": "Description of the playlist",
                "sharing": "Public or private",
                "track_ids": "List of track IDs to include in the playlist"
            },
            'method': 'POST',
            'url': "https://api.soundcloud.com/playlists",
            'static_params': {
                'Authorization': ''  # Replace with your actual token
            }
        },
        {
            'description': 'Update a SoundCloud playlist',
            'dynamic_params': {
                "playlist_id": "ID of the playlist to update",
                "track_ids": "Updated list of track IDs for the playlist"
            },
            'method': 'PUT',
            'url': "https://api.soundcloud.com/playlists/PLAYLIST_ID",  # PLAYLIST_ID should be replaced dynamically
            'static_params': {
                'Authorization': ''  # Replace with your actual token
            }
        }
    ]
)

# we are using llm_vm.client 
# we can connect our chatGPT to send the response to llm_vm 
# this is a LLM agent

