import qrcode
import qrcode.image.svg as svg

data = "https://www.exmple.com"

factory = svg.SvgImage

img = qrcode.make(data, image_factory=factory)

img.save("example.svg")