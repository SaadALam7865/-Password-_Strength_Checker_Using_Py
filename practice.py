

#   # Determine progress bar color & message
#     progress_bar_color = "red" # Default
#     if score == 4:
#         progress_bar_color = "green"
#         st.success('✅ Password is strong. 💪')
#     elif score == 3:
#         progress_bar_color = "yellow"
#         st.warning('⚠️ Your Password is medium strong. It could be stronger.')
#     else:
#         st.error('🔴 Your Password is weak. Consider using a more secure password.')
#      # Show progress bar
#     progress_bar = st.progress(score / 4)
#     # Strength Meter
#     strength_labels = ["🔴 Weak", "🟡 Medium", "🟢 Strong"]
#     strength_color = ["#FF4B4B", "#FFD700", "#4CAF50"]  # Red, Yellow, Green
#     strength_percentage = (score / 4)  # Convert score to percentage
#     progress_bar.progress(strength_percentage)
#     index = max(0, min(score - 1, 1))
#     st.markdown(f"<h3 style='color: {strength_color[index]};'> {strength_labels[index]} </h3>", unsafe_allow_html=True)


# import streamlit as st
# import re
# import secrets
# import string

# st.set_page_config(page_title='Password Strength Checker', page_icon='🔐')
# st.title('🔐 Password Strength Checker')
# st.markdown("""
# ## Welcome to the Password Strength Checker👋! 
# This tool helps you determine the strength of your password and provides suggestions for improvement. 🔐
# """)

# password = st.text_input('Enter Your Password', type='password')

# # Function to check password strength
# feedback = []
# score = 0

# if password:
#     # Check Length
#     if len(password) >= 8:
#         score += 1
#     else:
#         feedback.append('❌ Password must be at least 8 characters long.')

#     # Check Uppercase & Lowercase
#     if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
#         score += 1
#     else:
#         feedback.append('❌ Password must contain at least one uppercase and one lowercase letter.')

#     # Check Number
#     if re.search(r'\d', password):
#         score += 1  
#     else:
#         feedback.append('❌ Password must contain at least one number.')

#     # Check Special Character
#     if re.search(r'[!@#$%^&*]', password):
#         score += 1
#     else:
#         feedback.append('❌ Password must contain at least one special character.')

#     # Strength Feedback
#     if score == 4:
#         st.success('✅ Password is strong. 💪')
#         st.balloons()
#     elif score == 3:
#         st.warning('⚠️ Your password is medium strong. It could be stronger.')
#     else:
#         st.error('🔴 Your password is weak. Consider using a more secure password.')

#     # Common Passwords Check
#     common_passwords = ['password', '123456', 'qwerty', '12345678', 'admin', '1234567890', 'welcome', 'abc123', '123456789']
#     if password.lower() in common_passwords:
#         feedback.append('😥 Password is too common! Choose a unique one.')

#     # Show feedback
#     if feedback:
#         st.error('##### Password Check Results:')
#         for message in feedback:
#             st.write(message)

#     # Progress Bar
#     progress_bar = st.progress(score / 4)
#     strength_labels = ["🔴 Weak", "🟡 Medium", "🟢 Strong"]
#     strength_colors = ["#FF4B4B", "#FFD700", "#4CAF50"]  # Red, Yellow, Green
#     strength_percentage = score / 4
#     st.markdown(f"<h3 style='color: {strength_colors[score-1]};'>{strength_labels[score-1]}</h3>", unsafe_allow_html=True)

    # Suggest a Strong Password if Weak
#     if score < 4:
#         if st.button("💡 Suggest a Strong Password"):
#             def generate_strong_password():
#                 length = 12
#                 characters = string.ascii_letters + string.digits + "!@#$%^&*"
#                 return ''.join(secrets.choice(characters) for _ in range(length))

#             suggested_password = generate_strong_password()
#             st.text_input("Suggested Strong Password:", suggested_password)

# else:
#     st.info('Please enter a password to check its strength.')










#   # Determine progress bar color & message
#     progress_bar_color = "red" # Default
#     if score == 4:
#         progress_bar_color = "green"
#         st.success('✅ Password is strong. 💪')
#     elif score == 3:
#         progress_bar_color = "yellow"
#         st.warning('⚠️ Your Password is medium strong. It could be stronger.')
#     else:
#         st.error('🔴 Your Password is weak. Consider using a more secure password.')