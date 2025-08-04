# Music Whisper Transcriber

A simple Python tool to transcribe song lyrics and vocals from audio files using OpenAI's Whisper. Perfect for when you can't quite make out what the singer is saying!

## What it does

This tool helps you extract lyrics and vocals from music files by:
- Using OpenAI's Whisper AI model for accurate speech recognition
- Processing various audio formats (MP3, WAV, FLAC, M4A, etc.)
- Running completely offline - no internet connection required
- Providing clean, readable text output of the transcribed vocals

## Setup

1. **Clone or download this repository:**
```bash
git clone https://github.com/rkruk/Whisper-Transcriber.git
cd Whisper-Transcriber
```

2. **Create a Python virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install --upgrade pip
pip install openai-whisper
```

## Usage

**Basic usage:**
```bash
python transcribe.py path/to/your-song.mp3
```

**Examples:**
```bash
python transcribe.py ~/Music/song.mp3
python transcribe.py "/path/to/My Favorite Song.wav"
```

The transcription will be printed to your terminal. You can redirect it to a file if needed:
```bash
python transcribe.py song.mp3 > lyrics.txt
```

## Whisper Models

The tool uses the "base" model by default, which provides a good balance of speed and accuracy. You can modify `transcribe.py` to use different models:

- **tiny**: Fastest, least accurate (~39 MB)
- **base**: Good balance (default) (~74 MB)  
- **small**: Better accuracy (~244 MB)
- **medium**: Even better (~769 MB)
- **large**: Best accuracy (~1550 MB)

## Tips for Best Results

- **Clean audio works better**: Studio recordings typically transcribe more accurately than live performances
- **Instrumental sections**: The tool may output "[Music]" or attempt to transcribe background vocals during instrumental parts
- **Multiple languages**: The tool is set to English by default, but Whisper supports many languages
- **File formats**: Works with MP3, WAV, FLAC, M4A, and most common audio formats

## Troubleshooting

**If you get import errors:**
Make sure you're in your virtual environment:
```bash
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

**For very long songs:**
The transcription might take a few minutes for longer tracks. This is normal.

**Poor transcription quality:**
Try using a higher quality model by editing `transcribe.py` and changing `"base"` to `"small"` or `"medium"`.

## System Requirements

- Python 3.8+
- At least 1GB free RAM (more for larger models)
- Works on Linux, macOS, and Windows

## License

MIT License