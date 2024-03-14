from azure.storage.blob import BlobServiceClient

# Parameters for linking Azure to the application
storage_account_key = "zhrGpPBX6PVD+krncC4nVF4yoweEku/z2ErVxjLiuu/CjAVKqM5O4xlGWEyuWGxptL3mA1pv/6P4+AStjSjLEQ=="
storage_account_name = "useruploadhuggingface"
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
container_name = "useruploadhuggingfacevideo"
file_path = r"C:\Users\ASUS\Desktop\UoW\2ND YEAR\SDGP\HuggingFace\Video\production_id_5091624 (1080p).mp4"
file_name = "uploaded_video.mp4"


def uploadUserVideoToBlobStorage(file_path, file_name):
    """Uploads an MP4 video file to the specified Azure Blob Storage container and returns the URL.

    Args:
        file_path (str): The path to the MP4 video file.
        file_name (str): The desired name of the blob in Azure Blob Storage.

    Returns:
        str: The URL for the uploaded video file in Azure Blob Storage.

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

        # Open the video file in binary mode for upload
        with open(file_path, "rb") as data:
            # Upload the video data to the blob
            upload_blob_result = blob_client.upload_blob(data)

            # Get the URL for the uploaded blob
            blob_url = blob_client.url

            print(f"Video '{file_name}' uploaded successfully. URL: {blob_url}")
            return blob_url

    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}.")
        raise  # Re-raise the exception for further handling

if __name__ == "__main__":
    
    # Example usage
    uploaded_video_url = uploadUserVideoToBlobStorage(file_path, file_name)
    # You can now use the uploaded_video_url for further processing or sharing


