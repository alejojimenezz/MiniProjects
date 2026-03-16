import qrcode
import qrcode.image.svg as svg

with open("vCardData.txt", "r") as f:
    vcard = f.read().strip

factory = svg.SvgImage

img = qrcode.make(vcard, image_factory=factory)
img.save("QRGenerator/vcard.png")