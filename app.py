import gradio as gr
import os

def video_identity(video, text):    
    # You can use both the video and the text input in your function
    return video, text

demo = gr.Interface(video_identity,                     
                    [gr.Video(), gr.Textbox(label="Text 2", info="Text to compare", lines=3, value="")],                     
                    "playable_video",                     
                    examples=[[
                        os.path.join(os.path.dirname(__file__), "video/test_video.mp4"),
                        ""
                    ]],                     
                    cache_examples=True             
                    )

if __name__ == "__main__":    
    demo.launch()