from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Iron Man HUD is alive"}

# 🎬 VLC playback route
@app.get("/play/{filename}")
def play_media(filename: str):
    try:
        subprocess.Popen(["vlc", filename, "--intf", "dummy", "--play-and-exit"])
        return {"status": "playing", "file": filename}
    except Exception as e:
        return {"error": str(e)}

# 🔍 Radare2 analysis route
@app.get("/analyze/{binary}")
def analyze_binary(binary: str):
    try:
        result = subprocess.run(["r2", "-c", "aaa;afl", binary], capture_output=True, text=True)
        return {"analysis": result.stdout}
    except Exception as e:
        return {"error": str(e)}

