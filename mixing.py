import os
from pydub import AudioSegment

def mixingAudio(sound1_path, sound2_path,position):
  def check_and_convert(audio_file):
    """
    Checks file format and converts to supported format if necessary.
    """
    # Get file extension 
    extension = os.path.splitext(audio_file)[1].lower()
    if extension not in (".mp3", ".wav", ".flac"):
      # Convert to a supported format (e.g. mp3)
      sound = AudioSegment.from_file(audio_file)
      sound.export(os.path.splitext(audio_file)[0] + ".mp3", format="mp3")
      # Update filename to the converted one
      audio_file = os.path.splitext(audio_file)[0] + ".mp3"
    return audio_file

  # Check and convert audio files if needed
  sound1_path = check_and_convert(sound1_path)
  sound2_path = check_and_convert(sound2_path)

  # Load audio files
  sound1 = AudioSegment.from_file(sound1_path)
  sound2 = AudioSegment.from_file(sound2_path)

  # Mix sound2 with sound1, starting at 1000ms into sound1
  output = sound1.overlay(sound2, position)

  # Save the result (assuming mp3 format)
  output.export(r"mixedAudio\mixed_haptic_audioFile.mp3", format="mp3")
  return "The audio has been mixed."