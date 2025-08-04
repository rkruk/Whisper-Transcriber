# Whisper Transcriber

A minimal setup to transcribe audio files using OpenAI's Whisper locally in a Python virtual environment.

## Usage

1. Clone this repo:

```bash
git clone https://github.com/yourusername/whisper-transcriber.git
cd whisper-transcriber
```

2. Create and activate the virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install Whisper inside the venv:

```bash
pip install --upgrade pip
pip install git+https://github.com/openai/whisper.git
```

4. Run transcription:

```bash
python transcribe.py path/to/your-audio.mp3
```

5. To exit the virtual environment:

```bash
deactivate
```

## Notes

Tested on Gentoo Linux but should work on any POSIX system.

Whisper supports many audio formats.

Model choices: tiny, base, small, medium, large (default: base).

## License

MIT License
