import qrcode
img = qrcode.make('Something Deeply Hidden')#Some message here
img.save("Something Deeply Hidden.png")