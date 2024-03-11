import os
from pydub import AudioSegment

# Using raw strings to avoid issues with backslashes
sound1 = AudioSegment.from_mp3(r"audio\540553_badoink_bass-sine-pulse (mp3cut.net).mp3")
sound2 = AudioSegment.from_mp3(r"audio\y2mate.is - Cinematic Boom Sound Effect-_ttHanoHTL4-192k-1710149220_mastered.mp3")

# mix sound2 with sound1, starting at 1000ms into sound1)
output = sound1.overlay(sound2, position=1000)


# save the result
output.export(r"mixedAudio\mixed_haptic_audioFile.wav", format="mp3")


