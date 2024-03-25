import requests

index_counter = 0  # Global counter for video indexes

def videoAnalysis(sas_token, sas_url, search):
    
    global index_counter  # Access the global counter variable

    index_counter += 1
    index_name = f"video-index-{index_counter}"

    url = f"https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/{index_name}?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }

    data = {
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


    response = requests.put(url, json=data, headers=headers)
    
    #test code for errors
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)


    url_index = f"https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/{index_name}/ingestions/my-ingestion?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }


    data_index = {
        "videos": [
            {
                "mode": "add",
                "documentId": sas_token,
                "documentUrl": sas_url,
                "metadata": {
                    "cameraId": "camera1",
                    "timestamp": "2024-02-09 00:02:14"
                }
            }
        ]
    }

    response_index = requests.put(url_index, json=data_index, headers=headers)

    #test code for errors
    print("Index Ingestion - Response Status Code:", response_index.status_code)
    print("Index Ingestion - Response Content:", response_index.text)

    # Assuming you want to ingest another video with a different ingestion name
    url_new_ingestion = f"https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/{index_name}/ingestions/new-ingestion?api-version=2023-05-01-preview"

    data_new_ingestion = {
        "videos": [
            {
                "mode": "add",
                "documentId": "new_document_id",
                "documentUrl": "https://example.blob.core.windows.net/videos/new_video.mp4?sas_token_here",
                "metadata": {
                    "cameraId": "camera3"
                }
            }
        ]
    }

    response_new_ingestion = requests.put(url_new_ingestion, json=data_new_ingestion, headers=headers)

    #used to test code for errors
    print("New Ingestion - Response Status Code:", response_new_ingestion.status_code)
    print("New Ingestion - Response Content:", response_new_ingestion.text)


    url_query = f"https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/{index_name}:queryByText?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }

    data_query = {
        "queryText": search,
        "filters": {
            "stringFilters": [
                {
                    "fieldName": "cameraId",
                    "values": [
                        "camera1"
                    ]
                }
            ],
            "featureFilters": ["vision"]
        }
    }

    response_query = requests.post(url_query, json=data_query, headers=headers)

    if response_query.text == """{"error":{"code":"InvalidRequest","message":"Value for indexName is invalid."}}""":
        videoAnalysis(sas_token,sas_url, search)    
    else: 
        return response_query.text

#Enter the sas token
sas_token_1 = "sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D"
#the sas url
sas_url_1= "https://store1video.blob.core.windows.net/haptic-vid/test_video.mp4?sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D"
#query of what you are looking for 
instance_1 = "Explosion"

#Enter the sas token
sas_token_2 = "sp=r&st=2024-03-18T09:48:32Z&se=2026-07-02T17:48:32Z&spr=https&sv=2022-11-02&sr=b&sig=hLiFrDUtrutW9FWWRR7Z0Kbc4wkHs28YR9RXjVxw8uc%3D"
#the sas url
sas_url_2= "https://store1video.blob.core.windows.net/haptic-vid/desert_vehicle_test.mp4?sp=r&st=2024-03-18T09:48:32Z&se=2026-07-02T17:48:32Z&spr=https&sv=2022-11-02&sr=b&sig=hLiFrDUtrutW9FWWRR7Z0Kbc4wkHs28YR9RXjVxw8uc%3D"
#query of what you are looking for 
instance_2 = "Vehicle racing" 
