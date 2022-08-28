# import qrcode as qr
# image=qr.make("https://www.youtube.com/results?search_query=top+20+python+projects+for+beginner")
# image.save("my_mail.png")



##resize
import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://www.youtube.com/watch?v=8ext9G7xspg")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="Blue")
img.save("my_youtube.png")
