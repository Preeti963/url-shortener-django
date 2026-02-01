 # shortener/qr.py
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def generate_qr_code(url):
    """
    Generates a QR code image for the given URL and saves it to media/qr/
    Returns the file path for the QR image.
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)  # <-- THIS IS THE KEY: use full URL
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save to in-memory file
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    filename = f"qr/{url.split('/')[-1]}.png"  # unique name based on short code
    filebuffer = ContentFile(buffer.getvalue())

    # Save to MEDIA_ROOT using default storage
    saved_path = default_storage.save(filename, filebuffer)
    return saved_path  # this will be accessible via MEDIA_URL
