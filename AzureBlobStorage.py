from azure.storage.blob import BlobServiceClient

#parameters for linking azure to the application
storage_account_key="Q+EneUx5hlODHCjsSo49mm1bGVNdBd2wZ/T0yZMtag1C6FUIwr/yKf+XqDPmVF1PU81eitB2L3tN+AStD/eZ+A=="
storage_account_name="phonebrrdemonstration2"
connection_string="DefaultEndpointsProtocol=https;AccountName=phonebrrdemonstration2;AccountKey=Q+EneUx5hlODHCjsSo49mm1bGVNdBd2wZ/T0yZMtag1C6FUIwr/yKf+XqDPmVF1PU81eitB2L3tN+AStD/eZ+A==;EndpointSuffix=core.windows.net"
container_name="useruploadvideo"
file_path = r"C:\Users\ASUS\Desktop\UoW\2ND YEAR\SDGP\HuggingFace\Video\production_id_5091624 (1080p).mp4"
file_name = "uploaded_video.mp4"

def uploadUserVideoToBlobStorage(file_path,file_name):
    """Uploads an MP4 video file to the specified Azure Blob Storage container.

        Args:
            file_path (str): The path to the MP4 video file.
            file_name (str): The desired name of the blob in Azure Blob Storage.

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

        print(f"Video '{file_name}' uploaded successfully. Response: {upload_blob_result}")

    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}.")
        raise  # Re-raise the exception for further handling

if __name__ == "__main__":
    # Example usage
    uploadUserVideoToBlobStorage(file_path,file_name)

