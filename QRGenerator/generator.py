# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "qrcode[pil]>=8.2",
# ]
# ///

# Requires qrcode library
# Run 'pip install "qrcode[pil]"'
# Run 'pip install "qrcode[svg]"'

import qrcode
from PIL import Image

data = "https://docs.google.com/document/d/1qvt4YvwJa0hMZR4OmAT7LK3prnYxmUFf/edit?usp=sharing&ouid=101215009529947416218&rtpof=true&sd=true"

img = qrcode.make(data)

img.save("C:/Users/ThinkPad/Documents/VSCode/MiniProjects/QRGenerator/codeGenerated.png")
print("QR code generated and saved as codeGenerated.png")
