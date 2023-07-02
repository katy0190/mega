import qrcode

qrcode_img = qrcode.make('https://www.youtube.com/')
qrcode_img.save('./my_first_qrcode.png')


