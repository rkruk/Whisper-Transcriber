
---

## transcribe.py

```python
import sys
import whisper

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py path/to/audiofile")
        sys.exit(1)
    audio_path = sys.argv[1]
    model = whisper.load_model("base")
    print(f"Transcribing '{audio_path}' with Whisper (model: base)...")
    result = model.transcribe(audio_path, language="en")
    print("\n=== Transcription ===\n")
    print(result["text"])

if __name__ == "__main__":
    main()
