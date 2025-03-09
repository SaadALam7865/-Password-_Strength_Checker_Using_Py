
import streamlit as st
import re 
import secrets
import string

# Page Configuration
st.set_page_config(page_title='Password Strength Checker', page_icon='🔐')

# Custom CSS Styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #121212;
            color: white;
        }
        
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 8px #00ffcc;
        }
        .password-box {
            background-color: #222;
            padding: 10px;
            margin-top: 15px;
            hover:scale(1.5)
            color: white;
            border-radius: 10px;
            font-size: 1.2rem;
            box-shadow: 0px 0px 15px #00ffcc;
        }
        .progress-container {
            border-radius: 10px;
            padding: 5px;
            margin-top: 10px;
        }
        input[type="password"] {
            background-color: white;
            color: black;
            border: 5px
           
            border-radius: 8px;
            box-shadow: 0px 0px 10px #00ffcc;
            transition: all 0.3s ease-in-out;                    
    }
        /* Styling for the Suggest Password Button */
        .stButton > button {
            margin-top: 15px;
            background-color: #00ffcc !important;
            color: black !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 16px;
            box-shadow: 0px 0px 10px #00ffcc;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #00cc99 !important;
            box-shadow: 0px 0px 15px #00cc99;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Neon Glow Effect
st.markdown("<h1 class='title'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

st.markdown("""
## Welcome to the **Password Strength Checker** 👋  
This tool evaluates your password security & gives instant feedback. 🔐  
""")

# Input Field
password = st.text_input('Enter Your Password', type='password')

# Function to check password strength
feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('❌ Password must be at least **8 characters long**.')
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('❌ Password must contain **both uppercase and lowercase letters**.')
    
    if re.search(r'\d', password):
        score += 1  
    else:
        feedback.append('❌ Password must contain **at least one number**.')
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append('❌ Password must contain **at least one special character**.')

    # Determine progress bar color & message
    progress_bar_color = "red" # Default
    if score == 4:
        progress_bar_color = "green"
        st.success('✅ Password is strong. 💪')
        st.balloons()
    elif score == 3:
        progress_bar_color = "yellow"
        st.warning('⚠️ Your Password is medium strong. It could be stronger.')
    else:
        st.error('🔴 Your Password is weak. Consider using a more secure password.')
    
    strength_labels = ["🔴 Weak", "🟡 Medium", "🟢 Strong"]
    strength_colors = ["#FF4B4B", "#FFD700", "#4CAF50"]
    index = max(0, min(score - 1, 2))
    
    st.markdown(f"<h3 style='color: {strength_colors[index]};'> {strength_labels[index]} </h3>", unsafe_allow_html=True)
    
    st.progress(score / 4)
    
    if password.lower() in ['password', '123456', 'qwerty', '12345678', 'admin', '1234567890']:
        feedback.append('😥 Password is **too common!** Choose something unique.')
    
    if feedback:
        st.markdown("<h4 style='color: #ff6347;'>🔍 Password Check Results:</h4>", unsafe_allow_html=True)
        for message in feedback:
            st.markdown(f"<div class='password-box'>{message}</div>", unsafe_allow_html=True)
    
    if score < 4:
        if st.button("💡 Suggest a Strong Password"):
            def generate_strong_password():
                length = 12
                characters = string.ascii_letters + string.digits + "!@#$%^&*"
                return ''.join(secrets.choice(characters) for _ in range(length))
            
            suggested_password = generate_strong_password()
            st.text_input("Suggested Strong Password:", suggested_password)
else:
    st.info("🔍 **Enter a password to check its strength!**")
