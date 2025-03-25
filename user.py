import streamlit as st
import csv
import hashlib
import subprocess
import base64
import os

# Custom-styled title similar to the provided image
st.markdown(
    """
    <style>
    .title-container {
        background-color: #AAB2C5;  /* Light grayish-blue background */
        padding: 10px 20px;
        border-radius: 40px 0px 40px 0px !important; /* Top-left: Rounded, Top-right: Square, Bottom-right: Rounded, Bottom-left: Square */
        display: inline-block;
         overflow: hidden;
    }
    .title-text {
        font-size: 50px;
        font-weight: bold;
        color: black;
        font-family: Times New Roman, serif;
    }
    </style>
    <div class="title-container">
        <span class="title-text">Pneumonia Detection</span>
    </div>
    """,
    unsafe_allow_html=True
)


# Function to convert image to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image and apply styling
def set_background(image_file):
    if not os.path.exists(image_file):
        st.error(f"Background image not found: {image_file}")
        return

    bin_str = get_base64(image_file)
    page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-position: center;
            background-size: cover;
            background-repeat: no-repeat;
        }}

         /* Make the entire sidebar black */
        section[data-testid="stSidebar"] {{
            background-color: #252831 !important;
        }}

        /* Make Sidebar Black */
        .stSidebar, .css-1d391kg, .css-1v3fvcr {{
            background-color: black !important;
            color: white !important;
        }}

        /* Change all text to white */
        h1, h2, h3, h4, h5, h6, p, .stMarkdown, .stTextInput label, .stButton button, .stSelectbox label {{
            color: white !important;
        }}

        /* Change input boxes to black with white text */
        .stTextInput > div > div > input {{
            background-color: black !important;
            color: white !important;
            border: 1px solid white !important;
        }}

        /* Fix Password Inputs */
        .stTextInput > div > div > div > input {{
            background-color: black !important;
            color: white !important;
            border: 1px solid white !important;
        }}

        /* Change sign-up button background to black with white text */
        div.stButton > button:first-child {{
            background-color: black !important;
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid white !important;
            padding: 10px 20px !important;
        }}

        /* Fix Sidebar Dropdown */
        .stSelectbox > div > div {{
            background-color: black !important;
            color: white !important;
            border: 1px solid white !important;
        }}

        /* Remove Red Input Border */
        input:focus {{
            border: 1px solid white !important;
            outline: none !important;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set background image (Ensure the path is correct)
set_background("bgs/background.jfif")

# CSV file path to store user information
csv_file_path = "user_database.csv"
main_script_path = "streamlit/main.py"  # Path to the main script

# Ensure 'user_database' is initialized in session state
if 'user_database' not in st.session_state:
    st.session_state.user_database = []

# Function to save user credentials
def save_to_csv(username, hashed_password):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])

# Function to read stored credentials
def read_from_csv():
    if not os.path.exists(csv_file_path):
        return {}
    
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        return {row[0]: row[1] for row in reader}

# Function to hash passwords securely
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to launch main application script
def launch_main_script():
    subprocess.run(["streamlit", "run", main_script_path])

# Signup functionality
def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")

    if st.button("Sign Up"):
        if username and password and confirm_password:
            if password == confirm_password:
                user_database = read_from_csv()
                if username not in user_database:
                    hashed_password = hash_password(password)
                    save_to_csv(username, hashed_password)
                    st.success("✅ Account created successfully. Now you can log in.")
                else:
                    st.warning("⚠ Username already exists. Please choose a different one.")
            else:
                st.warning("⚠ Passwords do not match. Try again.")
        else:
            st.warning("⚠ All fields are required for sign-up.")

# Login functionality
def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In"):
        user_database = read_from_csv()
        if username in user_database:
            hashed_password = hash_password(password)
            if user_database[username] == hashed_password:
                st.success(f"✅ Welcome, {username}!")
                launch_main_script()
            else:
                st.error("❌ Invalid password. Try again.")
        else:
            st.error("❌ Invalid username. Try again.")

# Main function to handle navigation
def main():
    st.title("Login and Signup App")

    # Sidebar menu
    menu = ["Sign Up", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Sign Up":
        signup()
    elif choice == "Login":
        login()

if __name__ == "__main__":
    main()
