import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# --- Setup ---
st.set_page_config(page_title="Secure Data System", layout="centered")
st.title("🛡️ Secure Data Encryption System")

# Generate a Fernet key for encryption (in production, securely store and load this)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Initialize session state
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}  # { encrypted_text: { "encrypted_text": str, "passkey": hashed_str } }

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authorized" not in st.session_state:
    st.session_state.authorized = True  # True until user fails 3 times

# --- Utility Functions ---
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    record = st.session_state.stored_data.get(encrypted_text)
    
    if record and record["passkey"] == hashed:
        st.session_state.failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    else:
        st.session_state.failed_attempts += 1
        return None

# --- Navigation ---
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("🔍 Navigate", menu)

# --- Pages ---
if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.write("Use this system to **securely store** and **retrieve encrypted data** using a passkey.")
    st.markdown("---")
    st.info("Select 'Store Data' to save something, or 'Retrieve Data' to decrypt.")

elif choice == "Store Data":
    st.subheader("📥 Store New Data")
    data = st.text_area("Enter data to encrypt")
    passkey = st.text_input("Create a passkey", type="password")

    if st.button("Encrypt & Store"):
        if data and passkey:
            encrypted_text = encrypt_data(data)
            hashed_pass = hash_passkey(passkey)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_pass
            }
            st.success("✅ Data stored successfully!")
            st.code(encrypted_text, language="text")
        else:
            st.error("⚠️ Please enter both data and passkey.")

elif choice == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔒 You're locked out. Please reauthorize from the Login page.")
    else:
        st.subheader("🔓 Retrieve Data")
        encrypted_text = st.text_area("Paste the encrypted text")
        passkey = st.text_input("Enter your passkey", type="password")

        if st.button("Decrypt"):
            if encrypted_text and passkey:
                result = decrypt_data(encrypted_text, passkey)
                if result:
                    st.success("✅ Decryption successful!")
                    st.text_area("Your Decrypted Data", result, height=150)
                else:
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey. Attempts left: {remaining}")

                    if st.session_state.failed_attempts >= 3:
                        st.session_state.authorized = False
                        st.warning("🚫 Too many failed attempts. Go to Login page.")
            else:
                st.error("⚠️ Please fill in all fields.")

elif choice == "Login":
    st.subheader("🔑 Reauthorize Access")
    master_key = st.text_input("Enter master password", type="password")

    if st.button("Login"):
        if master_key == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Access restored. You can now retrieve data.")
        else:
            st.error("❌ Incorrect master password.")
