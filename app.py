import gradio as gr
import os
import requests

# Define your endpoint URL and subscription key
endpoint_url = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/my-video-index:queryByText?api-version=2023-05-01-preview"
subscription_key = "c54eec632ae5413e8075e3f825727822"

def video_identity(video):
    # Send a request to query the video index
    query_text = 'explosion'
    filters = {
        'stringFilters': [
            {
                'fieldName': 'cameraId',
                'values': ['camera1']
            }
        ],
        'featureFilters': ['vision']
    }
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
    data = {
        'queryText': query_text,
        'filters': filters
    }
    response = requests.post(endpoint_url, headers=headers, json=data)

    # Process the response
    if response.status_code == 200:
        result = response.json()  # Extract the result from the JSON response
        # Process the result here, you can modify this based on your requirements
        return result
    else:
        print("Failed to query video index. Status code:", response.status_code)
        print("Error message:", response.text)
        return None

demo = gr.Interface(video_identity, 
                    gr.Video(), 
                    "playable_video", 
                    examples=[
                        os.path.join(os.path.dirname(__file__), 
                                     "video/test_video.mp4")], 
                    cache_examples=True)

if __name__ == "__main__":
    demo.launch()
