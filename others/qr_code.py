
# pip install qrcode[pil] installing the library - [pil] is for pillow dependency for additional functionality

import qrcode

url = input("Enter the URL: ").strip()
file_path ="qr_code.png"
# saves next to the file

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
# This generates the image

img.save(file_path)

print("QR Code was generated!")