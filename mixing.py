import os
from pydub import AudioSegment

# Using raw strings to avoid issues with backslashes
sound1 = AudioSegment.from_wav(r"audio\mixkit-distant-explosion-1690.wav")
sound2 = AudioSegment.from_wav(r"audio\videoplayback_mastered (1).wav")

# mix sound2 with sound1, starting at 1000ms into sound1)
output = sound1.overlay(sound2, position=1000)


# save the result
output.export(r"mixedAudio\mixed_haptic_audioFile.wav", format="wav")

