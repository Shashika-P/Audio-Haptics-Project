import gradio as gr
import os

def video_identity(video):    
    return video

instructions = """
<b>Instructions:</b><br>
Step 1: Upload the example video to get the relevant timeframes that require haptics, the text query should be 'explosion'  <a href="https://portal.vision.cognitive.azure.com/demo/video-summary-and-frame-locator">Azure Cognitive Services Video Summary and Frame Locator</a> with explosions as the query.<br>
Step 2: Download the generated audio from <a href="https://phonebrrdemonstration2.blob.core.windows.net/audio3second0001/3_second_explosion_00001.flac">this ai-generated haptic audio</a>.
Step 3: Mix the Audio using any app of your choice and master the audio with <a href="https://aimastering.com/">ai-mastering program</a> 
"""

demo = gr.Interface(video_identity,                     
                    gr.Video(),                     
                    "playable_video",                     
                    examples=[os.path.join(os.path.dirname(__file__),                                      
                                     "video/test_video.mp4")],                     
                    cache_examples=True)

if __name__ == "__main__":    
    demo.launch(share=True)
