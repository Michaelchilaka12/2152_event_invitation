import qrcode
import os

def generate_qr_image_path(first_name, last_name):
    secret_code = "AB111"
    qr_data = f"{first_name} {last_name} | CODE: {secret_code}"

    qr = qrcode.make(qr_data)

    folder = "static/qrcodes"
    os.makedirs(folder, exist_ok=True)

    file_path = f"{folder}/{first_name}_{last_name}_qr.png"
    qr.save(file_path)

    return file_path
