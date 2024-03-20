import gradio as gr
import os
import AzureBlobStorageVideo
import AzureBlobStorageAudio


def predict_video(input_video, input_audio=None):
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
  
  #upload the video to AzureBlobStorage
  AzureBlobStorageVideo.uploadUserVideoToBlobStorage(input_video,"test6")
  
  """
  Processes the uploaded video (replace with your video analysis logic).

  Args:
      input_video: The uploaded video file object.
      input_audio (optional): The uploaded audio file object (MP3).

  Returns:
      A list containing the processed video and a message string.
  """
  # Placeholder processing (replace with actual video analysis)
  message = "**Placeholder:** Video processing not implemented yet."

  # You can optionally add a progress bar or loading indicator here

  if input_audio is None:
    return [input_video, message + " Generated Audio will be used"]
  AzureBlobStorageAudio.uploadUserAudioToBlobStorage(input_audio,"test8")
  return [input_video, message + f" Using uploaded audio: {input_audio.name}"]


css = """
#col-container {
  margin: 0 auto;
  max-width: 800px;
}
"""

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
        with gr.Column():
           audio_in = gr.File(label="Optional: Upload an Audio Track", file_types=[".mp3"])
        with gr.Column():
          video_out = gr.Video(label="Output Video")
          with gr.Row():
            text_out = gr.Textbox(label="Output Text")

  gr.Examples(
      examples=[[os.path.join(os.path.dirname(__file__), "video/test_video.mp4"),
                os.path.join(os.path.dirname(__file__), "video/audioTrack.mp3")]],
      fn=predict_video,
      inputs=[video_in, audio_in],
      outputs=[video_out, text_out],
      cache_examples= False  # Cache examples for faster loading
  )

  video_in.change(
      fn=predict_video,
      inputs=[video_in, audio_in],  # Use both video and audio inputs here
      outputs=[video_out, text_out],
      queue=False
    )

demo.launch(debug=True)