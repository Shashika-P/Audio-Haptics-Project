import gradio as gr
import os
import subprocess
# install moviepy dependency
moviepy = subprocess.run(["pip", "install", "moviepy"])
ffmpeg = subprocess.run(["pip", "install", "ffmpeg-python"])
pipUpdate = subprocess.run(["pip", "install", "--upgrade", "pip"])
from azure.storage.blob import BlobServiceClient
import AzureBlobStorageVideo
import AzureBlobStorageAudio
from apiTest import videoAnalysis
from Moviepy import extract_audio_from_video
from Moviepy import load_json_output
from Moviepy import get_explosion_segments
from Moviepy import create_final_audio
from Moviepy import save_audio
from Moviepy import without_audio
from Moviepy import combine_video_audio
from Moviepy import save_video
from moviepy.editor import *
import json

def predict_video(input_video, input_audio=None, input_choice="Explosions"):
  global filename, file_size  # Use the global keyword to refer to the global variables
  
  # Check if the video is available
  if input_video is None:
    return [None, "Please upload a video"]

  filename = input_video.name  # Get the uploaded filename
  file_size = os.path.getsize(input_video.name)  # Get the file size in bytes

  # Loop until a valid video is uploaded
  if not filename.lower().endswith('.mp4'):
    return [None, "Error: Please upload an MP4 video file."]

  if file_size > 20 * 1024 * 1024:
    return [None, "Error: The upload exceeds file size 16MB. Please upload a smaller file."]


  #Initialize blob storage credentials
  storage_account_name = "useruploadhuggingface"
  storage_account_key = "zhrGpPBX6PVD+krncC4nVF4yoweEku/z2ErVxjLiuu/CjAVKqM5O4xlGWEyuWGxptL3mA1pv/6P4+AStjSjLEQ=="
  connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

  video_container_name = "useruploadhuggingfacevideo"
  audio_container_name = "useruploadhuggingfaceaudio"

  # 1. Upload user video file to azure blob storage

  videoBlobURL = AzureBlobStorageVideo.uploadUserVideoToBlobStorage(input_video, filename)
  videoSASToken = AzureBlobStorageVideo.generateSASToken(storage_account_name,video_container_name, filename, storage_account_key)
  videoSASURL = AzureBlobStorageVideo.generateSASURL(storage_account_name, video_container_name, filename, videoSASToken)

  # 1.1. Upload user audio if available

  userAudioInputFlag = False

  if input_audio is not None:
        userAudioInputFlag = True
  else:
        if (input_choice == "Explosions"):
          input_audio = os.path.join(os.path.dirname(__file__), "audio/1_seconds_haptic_audio.mp3")
          print("explosion selected")
        elif (input_choice == "Lightning and Thunder"):
          input_audio = os.path.join(os.path.dirname(__file__), "audio/8_seconds_Thunder.mp3")
          print("lightning and thunder selected")
        elif (input_choice == "Vehicle Racing"):
          input_audio = os.path.join(os.path.dirname(__file__), "audio/5_seconds_vehicle_audio.mp3")
          print("vehicle racing selected")
        else:
          input_audio = os.path.join(os.path.dirname(__file__), "audio/5_seconds_haptic_videos.mp3")
          print("default selected")

  """
  Processes the uploaded video (replace with your video analysis logic).

  Args:
      input_video: The uploaded video file object.
      input_audio (optional): The uploaded audio file object (MP3).

  Returns:
      A list containing the processed video and a message string.
  """
  responseQueryText = videoAnalysis(videoSASURL, videoSASToken, input_choice)

  #	IF method returns error: run analysis again
  if responseQueryText == """{"error":{"code":"InvalidRequest","message":"Value for indexName is invalid."}}""":
      responseQueryText = videoAnalysis(videoSASURL, videoSASToken, input_choice)

  AzureBlobStorageVideo.delete_container('useruploadhuggingfacevideo')

  json_data = load_json_output(responseQueryText)

  # Extract audio from the video
  audio_path = extract_audio_from_video(input_video)
  # Get explosion segments
  explosion_segments = get_explosion_segments(json_data)

  print(input_audio)

  # Create final audio
  #final_audio = create_final_audio(audio_path, explosion_segments)
  final_audio = create_final_audio(audio_path, input_audio, explosion_segments)
  # Save enhanced audio
  finalAudioPath = "audio/finalAudio.mp3"
  save_audio(final_audio, finalAudioPath)

  if (userAudioInputFlag == True):
      AzureBlobStorageVideo.delete_container('useruploadhuggingfaceaudio')

  # Extract video without audio
  current_video = without_audio(VideoFileClip(input_video))

  # Combine video with final audio
  final_video = combine_video_audio(current_video, final_audio)

  # Save final video
  save_video(final_video, "video/final_enhanced_video.mp4")
  finalVideoPath = "video/final_enhanced_video.mp4"

  return [finalVideoPath, f"Video enhancement successful"]

css = """
#col-container {
  margin: 0 auto;
  max-width: 800px;
}
"""
video_1 = os.path.join(os.path.dirname(__file__), "video/test_video.mp4")
audio_1 = os.path.join(os.path.dirname(__file__), "audio/audioTrack.mp3")
search_1 = "Explosions"
with gr.Blocks(css=css) as demo:
  with gr.Column(elem_id="col-container"):
    gr.HTML("""
      <h2>Phone brr</h2>
      <h3>Welcome to the Hugging Face Space of Phone brr! We aim to create more immersive content for mobile phones with the use of haptic audio, this demo focuses on working for a very commonly used special effect of explosions hope you enjoy it.</h3>

      <p>Instructions:
        <br>Step 1: Upload your MP4 video.
        <br>Step 2: (Optional) Upload an MP3 audio track.
        <br>Step 3: We'll analyze the video and suggest explosion timeframes using Azure Cognitive Services (not included yet).
        <br>Step 4: Download haptic explosion audio from [link to audio source].
        <br>Step 5: Mix the Audio using any app of your choice and master the audio with an AI mastering program (links provided).
      </p>
    """)

  with gr.Row():
    with gr.Column():
      video_in = gr.File(label="Upload a Video", file_types=[".mp4"])
      with gr.Row():
        audio_in = gr.File(label="Optional: Upload an Audio Track", file_types=[".mp3"])
    with gr.Column():
      choice_in = gr.Dropdown(
            ["Explosions", "Lightning and Thunder", "Vehicle Racing"],value=callable(""),
            label="Choose", info="Haptic Audio will be added for the selected instance in a video",
            allow_custom_value=True          
        )
      with gr.Row():
        btn_in = gr.Button("Submit", scale=0)
    with gr.Column():
      video_out = gr.Video(label="Output Video")
      with gr.Row():
        text_out = gr.Textbox(label="Output Text")

  gr.Examples(
      examples=[[video_1,audio_1]],
      fn=predict_video,
      inputs=[video_in, audio_in,choice_in],
      outputs=[video_out, text_out],
      #cache_examples=True  # Cache examples for faster loading
  )
  with gr.Column():
    gr.HTML("""
            <h3> Audio Library </h2>
            <p> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/1_seconds_haptic_audio.mp3"> Explosion Audio Track 1 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/5_seconds_haptic_videos.mp3"> Explosion Audio Track 2 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/6_seconds_haptic_audio.mp3"> Explosion Audio Track 3 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/7_seconds_haptic_audio.mp3"> Explosion Audio Track 4 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/9_seconds_haptic_videos.mp3"> Explosion Audio Track 5 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/5_seconds_vehicle_audio.mp3"> Vehicle Audio Track 1 </a>
            <br> <a href="https://audiolibrary.blob.core.windows.net/audiolibrary/30_seconds_vehicle_audio.mp3"> Vehicle Audio Track 2 </a>
            </p>
            """)
    
  btn_in.click(
      fn=predict_video,
      inputs=[video_in,audio_in,choice_in],
      outputs=[video_out, text_out],
      queue=False
  )
demo.launch(debug=True)