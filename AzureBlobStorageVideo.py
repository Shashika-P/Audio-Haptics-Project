import azure.storage.blob  # Import required library
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

# Parameters for linking Azure to the application
storage_account_key = "zhrGpPBX6PVD+krncC4nVF4yoweEku/z2ErVxjLiuu/CjAVKqM5O4xlGWEyuWGxptL3mA1pv/6P4+AStjSjLEQ=="
storage_account_name = "useruploadhuggingface"
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
container_name = "useruploadhuggingfacevideo"
#file_path = r"C:\Users\isuru\Documents\IIT University\Modules\Year 2 - Semester 2\SDGP\HapticAudio SE09 Local Repo\gradio-env\HapticsProject\video\WIND ANIMATION.mp4"
#file_name = "wind_video.mp4"
target_container_id = 'useruploadhuggingfacevideo'



def deleteUserVideoFromBlobStorage(container_id: str) -> None:
    """
    Deletes all blobs within a specified Azure Blob Storage container.

    Args:
        container_id (str): The ID of the container to delete.
    """
    try:
        # Establish connection using your storage connection string (replace with yours)
        storage_connection_string = '<connection string>'
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
            upload_blob_result = blob_client.upload_blob(data, overwrite=True)

            # Get the URL for the uploaded blob
            blob_url = blob_client.url

            print(f"Video '{file_name}' uploaded successfully. URL: {blob_url}")
            return blob_url

    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}.")
        raise  # Re-raise the exception for further handling


def generateSASToken(account_name,container_name, blob_name, account_key):
    sas_token = generate_blob_sas(account_name=account_name,
                              container_name=container_name,
                              blob_name=blob_name,
                              account_key=account_key,
                              permission=BlobSasPermissions(read=True),
                              expiry=datetime.utcnow() + timedelta(hours=1))

    print(f"SAS Token generated:{sas_token}")

    return sas_token


def generateSASURL(account_name, container_name, blob_name, sas_token):

    sas_url = 'https://' + account_name + '.blob.core.windows.net/' + container_name + '/' + blob_name + '?' + sas_token
    print(f"SAS URL Generated: {sas_url}")

    return sas_url

if __name__ == "__main__":
    # Example usage
    uploaded_video_url = uploadUserVideoToBlobStorage(file_path, file_name)
    # use the uploaded_video_url for further processing or sharing
    # Retrieve container_client from within the upload function
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    target_container_id = 'useruploadhuggingfacevideo'
    deleteUserVideoFromBlobStorage(target_container_id)
