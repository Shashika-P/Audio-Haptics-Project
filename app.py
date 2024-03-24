import gradio as gr
import os
import subprocess
# install moviepy dependencies
moviepy = subprocess.run(["pip", "install", "moviepy"])
from azure.storage.blob import BlobServiceClient
import AzureBlobStorageVideo
import AzureBlobStorageAudio
from apiTest import sas_token_1
from apiTest import sas_url_1
from apiTest import videoAnalysis
from apiTest import instance_1
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



  # 1. Upload user video file to azure blob storage

  #AzureBlobStorageVideo.uploadUserVideoToBlobStorage(input_video, filename)

  #return [input_video, f" Using uploaded audio: {input_audio.name}"]
  #	IF user uploads audio file: upload audio file to blob storage
  # ELSE use default audio file from blob storage


  # message = "**Placeholder:** Video processing not implemented yet."
  #
  # if input_audio is not None:
  #     AzureBlobStorageAudio.uploadUserAudioToBlobStorage(input_audio, "test8")
  #     return [input_video, message + f" Using uploaded audio: {input_audio.name}"]
  # else:
  #     return [input_video, message + " Generated Audio will be used"]



  # 2. Analyze video and predict timestamps

  """
  Processes the uploaded video (replace with your video analysis logic).

  Args:
      input_video: The uploaded video file object.
      input_audio (optional): The uploaded audio file object (MP3).

  Returns:
      A list containing the processed video and a message string.
  """
 
  #responseQueryText = videoAnalysis(sas_url_1, sas_token_1, input_choice)

  #	IF method returns error: run analysis again
  #if responseQueryText == """{"error":{"code":"InvalidRequest","message":"Value for indexName is invalid."}}""":
  #    responseQueryText = videoAnalysis(sas_url_1, sas_token_1, input_choice)



  # 3. Use moviepy to add haptics to video

  #install masteringModule dependencies
  #os.chdir("masteringModule")
  #npminstall = subprocess.run(["npm", "install", "masteringModule/package.json"])
  #os.chdir("..")


  #	3.1. Extract audio from video
  #extractedAudioPath = extract_audio_from_video(input_video)

  #	3.2. Mix extracted audio with haptic audio

  # Load JSON output
  output_query_response = '{"value":[{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:16","end":"00:00:26","best":"00:00:21","relevance":0.4005849361419678},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:06","end":"00:00:16","best":"00:00:09","relevance":0.38852864503860474},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:42","end":"00:01:58","best":"00:01:43","relevance":0.38718080520629883},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:58","end":"00:02:14","best":"00:02:03","relevance":0.3811851143836975},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:42","end":"00:00:52","best":"00:00:42","relevance":0.3765566647052765},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:26","end":"00:00:42","best":"00:00:28","relevance":0.3718773126602173},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:08","end":"00:01:24","best":"00:01:10","relevance":0.3707084357738495},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:37","end":"00:01:42","best":"00:01:38","relevance":0.36235538125038147},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:29","end":"00:01:37","best":"00:01:33","relevance":0.3606133460998535},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:03","end":"00:01:08","best":"00:01:04","relevance":0.3513660728931427},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:00","end":"00:00:06","best":"00:00:05","relevance":0.3378048241138458}]}'  # JSON response


  json_data = load_json_output(output_query_response)

  # Extract audio from the video
  audio_path = extract_audio_from_video(input_video)
  # Get explosion segments
  explosion_segments = get_explosion_segments(json_data)

  # Create final audio
  final_audio = create_final_audio(audio_path, explosion_segments)

  # Save enhanced audio
  finalAudioPath = "audio/finalAudio.mp3"
  save_audio(final_audio, finalAudioPath)

  # Apply audio mastering

  master = subprocess.run(["node", "masteringModule/main.js", "--input", finalAudioPath, "--output", finalAudioPath])



  # Extract video without audio
  current_video = without_audio(VideoFileClip(input_video))

  # Combine video with final audio
  final_video = combine_video_audio(current_video, final_audio)

  # Save final video
  save_video(final_video, "video/final_enhanced_video.mp4")
  finalVideoPath = "video/final_enhanced_video.mp4"

  # 3.2.1. modify query response
  #hard-coded query response
  # output_query_response = '{"value":[{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:16","end":"00:00:26","best":"00:00:21","relevance":0.4005849361419678},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:06","end":"00:00:16","best":"00:00:09","relevance":0.38852864503860474},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:42","end":"00:01:58","best":"00:01:43","relevance":0.38718080520629883},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:58","end":"00:02:14","best":"00:02:03","relevance":0.3811851143836975},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:42","end":"00:00:52","best":"00:00:42","relevance":0.3765566647052765},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:26","end":"00:00:42","best":"00:00:28","relevance":0.3718773126602173},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:08","end":"00:01:24","best":"00:01:10","relevance":0.3707084357738495},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:37","end":"00:01:42","best":"00:01:38","relevance":0.36235538125038147},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:29","end":"00:01:37","best":"00:01:33","relevance":0.3606133460998535},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:01:03","end":"00:01:08","best":"00:01:04","relevance":0.3513660728931427},{"documentId":"sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D","documentKind":"VideoInterval","start":"00:00:00","end":"00:00:06","best":"00:00:05","relevance":0.3378048241138458}]}'  # JSON response
  # modifiedQueryResponse = load_json_output(output_query_response)
  #
  # # 3.2.2. get timestamps of haptics segments
  # hapticSegments = get_explosion_segments(modifiedQueryResponse)
  #
  # # 3.2.3. create final audio
  # finalAudio = create_final_audio(extractedAudioPath, hapticSegments)
  # finalAudioPath = "audio/finalAudio.mp3"
  # save_audio(finalAudio, finalAudioPath)
  #
  # #	3.3. Master final audio file
  # #master = subprocess.run(["node", "masteringModule/main.js", "--input", finalAudioPath, "--output", finalAudioPath])
  #
  # # 3.4. Prepare video file
  # #muteVideo = without_audio(input_video)
  # # currentVideoPath = "video/currentVideo.mp4"
  # # save_video(input_video, currentVideoPath)
  # # muteVideo = VideoFileClip(currentVideoPath)
  # # muteVideo = muteVideo.without_audio()
  # # mutevideoPath = "video/muteVideo.mp4"
  # # save_video(muteVideo, mutevideoPath)
  #
  # #	3.5. Combine audio with video
  # inputVideoPath = input_video
  # currentVideoPath = "video/currentVideo.mp4"
  # currentVideo = VideoFileClip(currentVideoPath)
  #
  # finalVideo = combine_video_audio(currentVideo,finalAudio)
  # finalVideoPath = "video/finalEnhancedVideo.mp4"
  # save_video(finalVideo, finalVideoPath)

  return [finalVideoPath, f"Video enhancement successful"]

  # You can optionally add a progress bar or loading indicator here


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
        <br>Step 1: Upload your video.
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
