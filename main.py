import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("https://www.linkedin.com/")
qr.png("qr_code.png",scale=8)