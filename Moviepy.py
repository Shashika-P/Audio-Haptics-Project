from moviepy.editor import *
import json

def load_json_output(output_query_response):
    # Convert JSON string to Python dictionary
    return json.loads(output_query_response)

def extract_audio_from_video(video_path):
    video = VideoFileClip(video_path)
    audio_path = "audio/current_audio.mp3"
    if video.audio is not None:
        video.audio.write_audiofile(audio_path)
        print("Audio file has been extracted from the video")
        return audio_path
    else:
        print("No audio found in the video.")
        return None

def get_explosion_segments(json_data):
    # creating an empty array for the results
    result = []
    # iterate over every explosion occurrence and find start, end, best values using the ml algorithm
    for i in json_data["value"]:
        result.append([i["start"], i["end"], i["best"]])

    # update start_explosion_time and end_explosion_time for each explosion occurrence
    for explosion in result:
        best_time = explosion[2]
        best_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], best_time.split(":")))
        start_explosion_time_seconds = best_time_seconds - 2
        end_explosion_time_seconds = best_time_seconds + 1
        explosion[0] = "{:02d}:{:02d}:{:02d}".format(start_explosion_time_seconds // 3600,
                                                     (start_explosion_time_seconds % 3600 // 60),
                                                     start_explosion_time_seconds % 60)
        explosion[1] = "{:02d}:{:02d}:{:02d}".format(end_explosion_time_seconds // 3600,
                                                     (end_explosion_time_seconds % 3600 // 60),
                                                     end_explosion_time_seconds % 60)
    return result

def create_final_audio(current_audio_path, haptic_audio_path, explosion_segments):
    current_audio = AudioFileClip(current_audio_path)  # location of the uploaded video
    # define the segments for the audio clips
    final_audio_segments = []
    #haptic_audio_path = haptic_audio_url
    haptic_audio = AudioFileClip(haptic_audio_path)

    # Iterate through each explosion occurrence and create audio segments
    for explosion in explosion_segments:
        best_explosion_time = explosion[2]
        best_explosion_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], best_explosion_time.split(":")))

        # Adjust the duration of the haptic audio to match the duration of the explosion
        haptic_audio_duration = haptic_audio.duration
        haptic_audio_clip = haptic_audio.subclip(0, haptic_audio_duration)

        # Create an audio clip starting from the best explosion time
        explosion_audio_clip = current_audio.subclip(best_explosion_time_seconds - 1,
                                                     best_explosion_time_seconds + haptic_audio_duration)

        # Concatenate the haptic audio clip with the explosion audio clip
        final_audio = concatenate_audioclips([explosion_audio_clip, haptic_audio_clip])
        final_audio_segments.append(final_audio)

    # concatenate final audio segments
    final_audio = concatenate_audioclips(final_audio_segments)
    # Match the audio duration with the video duration
    final_audio = final_audio.set_duration(current_audio.duration)
    return final_audio
    
def master_audio(audio_clip):
    # Apply audio mastering techniques here
    # Example: loudness normalization, equalization, compression, etc.
    # Replace the following line with your audio mastering process
    mastered_audio = audio_clip.fx(afx.audio_normalize)
    return mastered_audio

def save_audio(audio_clip, file_path):
    audio_clip.write_audiofile(file_path)
    print("Enhanced audio has been created")

def without_audio(video_clip):
    return video_clip.without_audio()

def combine_video_audio(video_clip, audio_clip):
    return video_clip.set_audio(audio_clip)

def save_video(video_clip, file_path):
    video_clip.write_videofile(file_path, fps=60)
    print("Final video has been created")

def process_video(current_video_path, output_query_response):
    json_data = load_json_output(output_query_response)
    audio_path = extract_audio_from_video(current_video_path)
    if audio_path:
        explosion_segments = get_explosion_segments(json_data)
        final_audio = create_final_audio(audio_path, explosion_segments)
        final_audio_mastered = master_audio(final_audio)
        save_audio(final_audio_mastered, "output.mp3")

        current_video = VideoFileClip(current_video_path)# Extracting audio from the video
        extracted_video = without_audio(current_video)

        final_video = combine_video_audio(extracted_video, final_audio_mastered)
        save_video(final_video, "final_video.mp4")



