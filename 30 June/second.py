import qrcode
img = qrcode.make('9874562.0')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")