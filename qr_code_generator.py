import qrcode
import streamlit as sl

# Prompt the user for the data to encode in the QR code
data = input("Enter the data to encode in the QR code: ")
# Create a QRCode object with customizable parameters
qr = qrcode.QR(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,  # Higher error correction for added reliability
    box_size=10,
    border=4,
)
# Add the user-provided data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Specify custom colors for the QR code and background
fill_color = input("Enter the QR code color (e.g., 'blue', '#FF0000', etc.): ")
back_color = input("Enter the background color (e.g., 'white', '#00FF00', etc.): ")

# Create the QR code image with the user-specified colors
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save the QR code image with a custom filename
filename = input("Enter the filename to save the QR code (e.g., 'my_qr_code.png'): ")
img.save(filename)

print(f"The QR code with the data '{data}' has been generated and saved as '{filename}'.")
