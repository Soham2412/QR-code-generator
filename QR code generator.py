import qrcode
url=input("enter URL:")
img=qrcode.make(url)
img.save('qrcode.png')
print('QR code generated')
