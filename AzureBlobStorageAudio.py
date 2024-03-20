from azure.storage.blob import BlobServiceClient

# Replace placeholders with your actual credentials
storage_account_name = "useruploadhuggingface"
storage_account_key = "zhrGpPBX6PVD+krncC4nVF4yoweEku/z2ErVxjLiuu/CjAVKqM5O4xlGWEyuWGxptL3mA1pv/6P4+AStjSjLEQ=="
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

container_name = "useruploadhuggingfaceaudio"  # Update container name for audio files
file_path = r"C:\Users\ASUS\Desktop\UoW\2ND YEAR\SDGP\AUDIO\edit\3_second_audio.flac"  # Update path to your MP3 file
file_name = "uploaded_audio.mp3"

def deleteUserAudioFromBlobStorage(blob_client):
    """Deletes the specified blob from Azure Blob Storage.

    Args:
        blob_client (BlobClient): The BlobClient object for the blob to delete.
    """
    try:
        blob_client.delete_blob()
        print(f"Audio deleted successfully from Azure Blob Storage.")
    except Exception as e:
        print(f"Error deleting audio: {e}")

def uploadUserAudioToBlobStorage(file_path, file_name):
    """Uploads an MP3 audio file to the specified Azure Blob Storage container and returns the URL.

    Args:
        file_path (str): The path to the MP3 audio file.
        file_name (str): The desired name of the blob in Azure Blob Storage.

    Returns:
        str: The URL for the uploaded audio file in Azure Blob Storage.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """

    try:
        # Create BlobServiceClient using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)

        # Get a reference to the blob container
        container_client = blob_service_client.get_container_client(container_name)

        # Create the blob client with the specified file name
        blob_client = container_client.get_blob_client(file_name)

        # Open the audio file in binary mode for upload
        with open(file_path, "rb") as data:
            # Upload the audio data to the blob
            upload_blob_result = blob_client.upload_blob(data)

            # Get the BlobClient object for deleting process
            blob_client = container_client.get_blob_client(file_name)

            # Get the URL for the uploaded blob
            blob_url = blob_client.url

            print(f"Audio '{file_name}' uploaded successfully. URL: {blob_url}")
            return blob_url

    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}.")
        raise  # Re-raise the exception for further handling


if __name__ == "__main__":
    # Example usage
    uploaded_audio_url = uploadUserAudioToBlobStorage(file_path, file_name)
    # use the uploaded_audio_url for further processing or sharing
        # receive the enhanced video:
    deleteUserAudioFromBlobStorage(blob_client)
