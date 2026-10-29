# 🔐 AI Cryptography Basics Tutor

A beginner-friendly Python mini project that demonstrates core cryptography concepts with an interactive Streamlit interface.

> **Note:** This is an educational demo, not an AI-powered system and not a production security tool. The name describes the tutor-style learning experience. Classical cipher and Base64 features are intentionally included for learning only.

## Features
- Learn key cryptography vocabulary
- Encrypt/decrypt text using a Caesar Cipher
- Encode/decode Base64 (clearly labeled as encoding, not encryption)
- Generate a SHA-256 digest for sample text
- Encrypt/decrypt text with Fernet authenticated symmetric encryption

## Tech stack
- Python
- Streamlit
- Python `cryptography` package

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (recommended).

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Start the app:
```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Upload to GitHub

1. Create a new repository on GitHub named `ai-cryptography-basics-tutor`.
2. Extract this project ZIP.
3. Open a terminal in the extracted folder and run:

```bash
git init
git add .
git commit -m "Initial commit: AI Cryptography Basics Tutor"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-cryptography-basics-tutor.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not upload secrets or private keys.

## Deploy online (optional)
You can deploy the repository using Streamlit Community Cloud:
1. Sign in to Streamlit Community Cloud.
2. Connect GitHub and choose this repository.
3. Select `app.py` as the main file.
4. Deploy.

## Security notes
- Caesar Cipher is not secure.
- Base64 is reversible encoding, not encryption.
- SHA-256 alone is not suitable for storing passwords.
- Fernet uses a key: anyone with that key can decrypt the data. The demo key is generated for the current app session and should not be used for real secrets.
- Never enter real passwords or sensitive information into a classroom demo.

## Project structure
```text
ai-cryptography-basics-tutor/
├── app.py
├── requirements.txt
└── README.md
```

## Future improvements
- Add quizzes and scoring
- Add visual step-by-step cipher explanations
- Add an AI API for conversational tutoring
- Add unit tests and accessibility improvements

## License
For educational use. Add a license file if you want to specify reuse terms.
