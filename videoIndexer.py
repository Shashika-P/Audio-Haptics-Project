import requests

# Define your endpoint URL and subscription key
endpoint_url = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes?api-version=2023-05-01-preview"
subscription_key = "c54eec632ae5413e8075e3f825727822"

# Define the request headers
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

# Define the request body for creating the video index
body = {
    "name": "my-video-index",
    "metadataSchema": {
        "fields": [
            {
                "name": "cameraId",
                "searchable": False,
                "filterable": True,
                "type": "string"
            },
            {
                "name": "timestamp",
                "searchable": False,
                "filterable": True,
                "type": "datetime"
            }
        ]
    },
    "features": [
        {
            "name": "vision",
            "domain": "surveillance"
        },
        {
            "name": "speech"
        }
    ]
}

# Send the request to create the video index
response = requests.put(endpoint_url, headers=headers, json=body)

# Check if the request was successful
if response.status_code == 200:
    print("Video index created successfully.")
else:
    print("Failed to create video index. Status code:", response.status_code)
    print("Error message:", response.text)