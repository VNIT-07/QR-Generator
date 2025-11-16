import streamlit as st
import qrcode
from urllib.parse import urlparse
import re
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("QR Code Generator")

url = st.text_input("Enter URL", value="https://www.youtube.com/watch?v=pJdTyvufOdg").strip()
if not url:
    st.info("Type a URL above.")
else:
    parsed = urlparse(url)
    host = parsed.netloc or parsed.path
    clean = re.sub(r'[^A-Za-z0-9._-]+', '_', host).strip('_')
    filename = f"{clean or 'qrcode'}.png"
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    st.image(img)
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.download_button(
        label="Download QR as PNG",
        data=buf,
        file_name=filename,
        mime="image/png"
    )

    st.write("Saved filename (suggested):", filename)
