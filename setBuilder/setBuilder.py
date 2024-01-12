# import our client
from llm_vm.client import Client
import os

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

