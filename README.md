---
title: HapticsProject
emoji: 🐠
colorFrom: red
colorTo: indigo
sdk: gradio
sdk_version: 4.7.1
app_file: app.py
pinned: false
license: unknown
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Phone Brr

This project empowers you to create engaging videos with haptic feedback seamlessly integrated. Leverage the power of Azure Video Analysis and Summary, MoviePy for video processing, and Gradio for an intuitive web user interface.

Link to the Hugging Face Space: https://huggingface.co/spaces/SE-09/HapticsProject

## Features

- **AI-powered Haptic Integration:** Intelligently identify video segments that benefit from haptic effects using Azure Video Analysis and Summary.
- **Effortless Video Editing:** Utilize MoviePy's capabilities for efficient video processing and precise editing.
-  **Curated Haptic Library:** Store and manage haptic audio clips in Azure Blob Storage for flexible incorporation into your videos.
- **Web-based Interface:** Gradio provides a user-friendly web UI where you can effortlessly upload videos, select haptic audio clips, and generate the final enhanced video.
- **Audio Mastering:** Add a final touch of polish with AI-powered audio mastering to ensure a well-balanced and professional sound.


## Installation

**Prerequsites:** Ensure you have Python 3.8 or higher installed along with the required libraries:
- ` azure-cognitiveservices-videoanalyzer `
- ` moviepy `
- ` gradio `
- ` requests `
- ` pydub `
- ` ffmprg `
- ` subprocess `
    - You can install them using
```bash
  pip install azure-cognitiveservices-videoanalyzer moviepy gradio requests pydub ffmprg subprocess
```
    
## Usage

1. **Clone the Repository:** 
-   Use `git clone https://huggingface.co/spaces/SE-09/HapticsProject` to clone the Repository locally.
2. **Configuration:**
-   Set up a gradio virtual environment following [these steps](https://www.gradio.app/guides/installing-gradio-in-a-virtual-environment) before installing gradio.
-   Install the remianing python libraries and dependancies.
3. **Video Editing and Haptic Audio Integration:**
-   Upload a Video file using the web interface.
-   Additional optional Input fields to upload a custom Audio track along with specifying the instance to add haptics to.
-   Click "Submit" button.
4. **Output:** 
-   Upon sucessful processing the output fields will preview a video that can be downloaded.



## Authors

- [@Hussain](https://github.com/HussainLatiff)
- [@Ravija](https://github.com/ravijaanthony)
- [@Shashika](https://github.com/Shashika-bit)
- [@Banuka](https://github.com/BanukaMandinu)
- [@Isuru](https://github.com/isururana)



