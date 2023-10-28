import qrcode

# Function to generate and save QR codes with owner information
def generate_qr_code(owner_name, drone_id, output_path):
    # Combine owner name and drone ID as the QR code content
    qr_code_content = f"Owner: {owner_name}\nDrone ID: {drone_id}"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code_content)
    qr.make(fit=True)
    
    # Create an Image object from the QR code data
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    qr_img.save(output_path)

# Example usage:
owner_name = "John Doe"
drone_id = "123456"
output_path = "drone_qr_code.png"

generate_qr_code(owner_name, drone_id, output_path)
print(f"QR code generated and saved as {output_path}")

