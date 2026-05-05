import qrcode
qr=qrcode.QRCode()
a="Manasvi is nice"
qr.add_data(a)
qr.make(fit=True)
res=qr.make_image(fill_color="red",back_color="white")
res.save("manasvi.png")
print("QR code created")
