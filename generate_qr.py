import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_qr_code(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

    log_message = f"QR Code generated successfully.\nData: {url}"
    log_image = Image.new("RGB", (500, 100), color="white")
    draw = ImageDraw.Draw(log_image)

    try:
        font = ImageFont.load_default()
    except IOError:
        font = None

    draw.text((10, 10), log_message, fill="black", font=font)
    log_image.save("log_image.png")
    print("Log saved as log_image.png")

if __name__ == "__main__":
    create_qr_code("https://github.com/auroog")
