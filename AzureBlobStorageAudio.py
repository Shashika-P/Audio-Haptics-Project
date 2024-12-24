
from azure.storage.blob import BlobServiceClient

# Replace placeholders with your actual credentials
storage_account_name = ""
storage_account_key = ""
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

container_name = ""  # Update container name for audio files


def delete_container(container_id: str) -> None:
  """
  Deletes all blobs within a specified Azure Blob Storage container.

  Args:
      container_id (str): The ID of the container to delete.
  """
  try:
    # Establish connection using your storage connection string (replace with yours)
    storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=  ;AccountKey=  ;EndpointSuffix=core.windows.net'
    blob_service_client = azure.storage.blob.BlobServiceClient.from_connection_string(storage_connection_string)

    # Get container client
    container_client = blob_service_client.get_container_client(container_id)

    # Delete all blobs in the container (iterator for large datasets)
    blobs = container_client.list_blobs()
    for blob in blobs:
        container_client.delete_blob(blob.name)
    print(f'Container "{container_id}" emptied successfully.')

  except Exception as e:
    print(f'Error deleting blobs: {e}')


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
            # Upload the audio data to the blob allowing overwrites
            upload_blob_result = blob_client.upload_blob(data, overwrite=True)


            # Get the URL for the uploaded blob
            blob_url = blob_client.url

            print(f"Audio '{file_name}' uploaded successfully. URL: {blob_url}")
            return blob_url  # Only return the URL

    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}.")
        raise  # Re-raise the exception for further handling


if __name__ == "__main__":
    # Example usage
    uploaded_audio_url = uploadUserAudioToBlobStorage(file_path, file_name)
    # use the uploaded_audio_url for further processing or sharing

    # Retrieve container_client from within the upload function
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Pass container_client and file_name to the deletion function
    delete_container('')
