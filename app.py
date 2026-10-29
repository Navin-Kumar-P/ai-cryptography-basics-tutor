import streamlit as st
from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib

st.set_page_config(page_title="AI Cryptography Basics Tutor", page_icon="🔐", layout="centered")

st.title("🔐 AI Cryptography Basics Tutor")
st.write("A beginner-friendly mini project to learn classical and modern cryptography concepts.")
st.info("Educational demo only. Do not use this app to protect real-world secrets.")

tabs = st.tabs(["Learn", "Caesar Cipher", "Base64", "Password Hashing", "Fernet Encryption"])

with tabs[0]:
    st.header("Cryptography in simple words")
    st.write("Cryptography protects information by transforming it so that only an intended recipient can read it.")
    st.subheader("Core concepts")
    st.markdown("""
    - **Plaintext:** the original readable message.
    - **Ciphertext:** the transformed, unreadable-looking message.
    - **Encryption:** converting plaintext into ciphertext using an algorithm and key.
    - **Decryption:** converting ciphertext back into plaintext.
    - **Hashing:** creating a one-way digest, commonly used for integrity checks.
    - **Encoding:** changing a representation; it is not encryption and does not provide secrecy.
    """)
    st.warning("Caesar Cipher and Base64 are learning examples, not secure protection methods.")

with tabs[1]:
    st.header("Caesar Cipher")
    st.caption("Shifts each English letter by a chosen number. Non-letters stay unchanged.")
    message = st.text_area("Enter a message", "Hello, world!", key="caesar_message")
    shift = st.slider("Shift amount", 0, 25, 3)
    mode = st.radio("Action", ["Encrypt", "Decrypt"], horizontal=True)
    def caesar(text, amount):
        result = []
        for char in text:
            if "a" <= char <= "z":
                result.append(chr((ord(char) - ord("a") + amount) % 26 + ord("a")))
            elif "A" <= char <= "Z":
                result.append(chr((ord(char) - ord("A") + amount) % 26 + ord("A")))
            else:
                result.append(char)
        return "".join(result)
    actual_shift = shift if mode == "Encrypt" else -shift
    st.text_area("Result", caesar(message, actual_shift), height=100)

with tabs[2]:
    st.header("Base64 encoding")
    st.caption("Base64 is encoding, not encryption. Anyone can decode it.")
    text = st.text_area("Text to encode", "Cryptography is interesting!", key="b64_text")
    if st.button("Encode to Base64"):
        st.code(base64.b64encode(text.encode("utf-8")).decode("ascii"))
    encoded = st.text_input("Base64 text to decode")
    if st.button("Decode Base64"):
        try:
            decoded = base64.b64decode(encoded, validate=True).decode("utf-8")
            st.success(decoded)
        except (ValueError, UnicodeDecodeError):
            st.error("Invalid Base64 input or decoded text is not UTF-8.")

with tabs[3]:
    st.header("SHA-256 Hashing")
    st.caption("Hashing is one-way: a hash is not decrypted back into the original text.")
    password = st.text_input("Enter sample text to hash", type="password")
    if st.button("Generate SHA-256 hash"):
        digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
        st.code(digest)
        st.write("For real password storage, use a password-hashing function such as Argon2id, scrypt, or bcrypt with salts—not plain SHA-256.")

with tabs[4]:
    st.header("Fernet symmetric encryption")
    st.write("Fernet provides authenticated symmetric encryption. The key must be kept secret.")
    if "fernet_key" not in st.session_state:
        st.session_state.fernet_key = Fernet.generate_key()
    st.code(st.session_state.fernet_key.decode("ascii"), language=None)
    st.caption("Demo key for this session. Copy and store it securely if you want to decrypt later.")
    secret = st.text_area("Message to encrypt", "This is a private message.", key="fernet_message")
    if st.button("Encrypt message"):
        f = Fernet(st.session_state.fernet_key)
        token = f.encrypt(secret.encode("utf-8")).decode("ascii")
        st.session_state.last_token = token
        st.code(token)
    token_input = st.text_area("Token to decrypt", st.session_state.get("last_token", ""), key="token_input")
    if st.button("Decrypt token"):
        try:
            plaintext = Fernet(st.session_state.fernet_key).decrypt(token_input.encode("ascii")).decode("utf-8")
            st.success(plaintext)
        except (InvalidToken, ValueError, UnicodeDecodeError):
            st.error("Could not decrypt. Check the token and ensure it was created with the current session key.")

st.divider()
st.caption("Mini Project • Python + Streamlit • Built for learning")
