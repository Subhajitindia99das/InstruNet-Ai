import sqlite3
import bcrypt
import streamlit as st

# 1. Database Initialization
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 2. Security Functions (Hashing Passwords)
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# 3. Database Operations
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        return True # Success
    except sqlite3.IntegrityError:
        return False # Username already exists
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return verify_password(password, result[0])
    return False

# 4. The UI Function
def show_auth_page():
    init_db() # Ensure DB exists when the page loads
    
    st.markdown("<h1 style='text-align: center; color: #a1a1aa;'>🎵 InstruNet AI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #e2e2f0;'>Welcome! Please Login or Register</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create center columns so the login box isn't too wide
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        # --- LOGIN TAB ---
        with tab1:
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login", use_container_width=True):
                if authenticate_user(login_username, login_password):
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = login_username
                    st.success("Logged in successfully!")
                    st.rerun() # Refresh the page to load the main app
                else:
                    st.error("Invalid username or password")
                    
        # --- REGISTER TAB ---
        with tab2:
            reg_username = st.text_input("New Username", key="reg_username")
            reg_password = st.text_input("New Password", type="password", key="reg_password")
            reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
            
            if st.button("Register Account", use_container_width=True):
                if reg_password != reg_confirm:
                    st.error("Passwords do not match!")
                elif len(reg_username) < 3 or len(reg_password) < 6:
                    st.error("Username must be at least 3 characters and password 6 characters.")
                else:
                    if create_user(reg_username, reg_password):
                        st.success("Account created successfully! You can now log in.")
                    else:
                        st.error("Username already exists. Please choose another one.")