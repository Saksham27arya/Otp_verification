import os
import math
import random
import smtplib

# Function to generate a random OTP of a given length
def generate_otp(length=6):
    digits = "0123456789"
    otp = "".join([random.choice(digits) for _ in range(length)])
    return otp

# Generate a 6-digit OTP
otp = generate_otp()

# Message to be sent via email
otp_message = otp + " is your OTP"

# Set up the SMTP connection
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = "your.email@example.com"  # Change to your Gmail account
app_password = "your_app_password"  # Use an app-specific password

# Initialize the SMTP session
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()  # Secure the SMTP connection
smtp.login(sender_email, app_password)  # Log in with the Gmail account

# Send the OTP email
recipient_email = input("Enter your email: ")
smtp.sendmail(sender_email, recipient_email, otp_message)

# Ask the user to enter the OTP they received
user_input_otp = input("Enter Your OTP >>: ")

# Verify the OTP
if user_input_otp == otp:
    print("Verified")
else:
    print("Please check your OTP again.")

# Close the SMTP connection
smtp.quit()
