# Requires qrcode library
# Run 'pip install "qrcode[pil]"'
# Run 'pip install "qrcode[svg]"'

import qrcode
from PIL import Image

data = "https://www.google.com/"

img = qrcode.make(data)

img.save("QRGenerator/codeGenerated.png")
print("QR code generated and saved as codeGenerated.png")