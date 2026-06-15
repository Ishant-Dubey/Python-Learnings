import qrcode
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

data= str(input("Enter a URL or a string : ") or "https://x.com/Ishant25Dubey")

file_name = str(input("Set your desired file name : ") or "QRCode")
final_file_name = '{}.png'.format(file_name)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(final_file_name)