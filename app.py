import gradio as gr
import os  

isFileType = False # To return true if the file type is 'mp4'
isFileSize = False # To return true if the file > 16mb

# Validate the video file
def predict_video(input_video):
    filename = input_video.name  # Get the uploaded filename
    file_size = os.path.getsize(input_video) # Get the file size in bytes

    # Check if it's not an MP4 file
    if not filename.lower().endswith('.mp4'):
        isFileType = True
        return "Error: Please upload an MP4 video file."
    
    # Checks if the file is above 16mb
    if file_size > 16 *1024 * 1024: # 1mb = 1024bytes
        isFileSize = True
        return "Error: The upload exceeds file size 16MB. Please upload a smaller file."

    # Your processing code here (if the file type is correct)
    return "Video processed successfully!"

inputs = gr.File(label="Upload a video")
output = gr.Textbox()

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Phone brr
    Welcome to the Hugging face Space of Phone brr we aim to create more immersive content for mobile phones with the use of haptic audio, this demo focuses on working for a very commonly used special effect of explosions hope you enjoy it.

    Instructions
     
    Step 1: Upload the example video to get the relevant timeframes that require haptics <a href="https://portal.vision.cognitive.azure.com/demo/video-summary-and-frame-locator">Azure Cognitive Services Video Summary and Frame Locator</a> with explosions as the query.

    Step 2: Download the generated audio from <a href="https://phonebrrdemonstration2.blob.core.windows.net/audio3second0001/3_second_explosion_00001.flac">this ai-generated haptic audio</a>.

    Step 3: Mix the Audio using any app of your choice and master the audio with <a href="https://aimastering.com/">ai-mastering program</a> 

    """),

    gr.Interface(fn=predict_video, inputs=inputs, outputs=output).launch()

if __name__ == "__main__":    
    demo.launch(share=True)
