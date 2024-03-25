import subprocess

def masterAudio(inputPath,outputPath):
    try:
        master = subprocess.run(["node", "masteringModule/main.js", "--input", inputPath, "--output", outputPath])
    except subprocess.CalledProcessError as err:
        print("Error running Mastering Module: ", err)