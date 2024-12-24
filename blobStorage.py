from azure.storage.blob import BlobServiceClient
from io import BytesIO
from pydub import AudioSegment
import os
import ffmpeg

audio_clip_mapping = {
    "key1": "    ",
    # Add more key-value pairs as needed
}

# Initialize Azure Blob Storage client
account_name = '    '
account_key = '    '

blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net",
    credential=account_key
)

# Define the container name
container_name = '    ' 

# Define a function to retrieve audio clips by key
def retrieve_audio_clip(key):
    # Get the blob name corresponding to the key
    blob_name = audio_clip_mapping.get(key)
    if blob_name is None:
        print(f"No audio clip found for key: {key}")
        return None

    # Get the blob client for the audio clip
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Stream the audio data directly into an AudioSegment object
    stream = BytesIO()
    blob_client.download_blob().download_to_stream(stream)
    stream.seek(0)

    audio_segment = AudioSegment.from_file(stream)
    stream.close()  # Close the stream to avoid memory leaks
    return audio_segment

# Example usage:
key_to_retrieve = "key1"
retrieved_audio_clip = retrieve_audio_clip(key_to_retrieve)

if retrieved_audio_clip:
    print(f"Retrieved audio clip for key {key_to_retrieve}")
    # Further process retrieved_audio_clip as needed
