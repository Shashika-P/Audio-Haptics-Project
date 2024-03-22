import subprocess
#input path  of audio file
#inPath = "audioTracks/CinematicBoom.mp3"

#desired path of output
#outPath = "masteredAudio/CinematicBoomMastered.mp3"

# try:
#     output = subprocess.check_output(["node", "masteringModule/main.js", "--input", inputPath, "--output", outputPath])
#     print(output.decode())
# except subprocess.CalledProcessError as e:
#     print("Error running JavaScript file:", e)


def masterAudio(inputPath,outputPath):
    try:
        master = subprocess.run(["node", "masteringModule/main.js", "--input", inputPath, "--output", outputPath])
    except subprocess.CalledProcessError as err:
        print("Error running Mastering Module: ", err)

# testing
# masterAudio(inputPath,outputPath)