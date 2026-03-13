# Requires qrcode library
# Run 'pip install "qrcode[pil]"'

import qrcode

data = "https://www.instagram.com/"
img = qrcode.make(data)

img.save("QRGenerator/codeGenerated.png")
print("QR code generated and saved as codeGenerated.png")