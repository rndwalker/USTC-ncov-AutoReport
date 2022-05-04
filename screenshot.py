import base64
import io
import random

import qrcode
from PIL import Image
from constant import logo_base64


def generate_akm(token=None):
	logo = Image.open(io.BytesIO(base64.decodebytes(bytes(logo_base64, "utf-8"))))
	random.seed()
	if not token:
		token = random.randbytes(16).hex()
	url = 'https://akm.ahzwfw.gov.cn/akm-sj-mgr/index.html#/myAkm?isScan=1&id=akm:qrcode:{}&cityNo=340000000000' \
		.format(token)
	qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, border=0, box_size=10)
	qr.add_data(url)
	qr.make(fit=True)
	code = qr.make_image(fill_color="#5cb83d", back_color="white").convert("RGBA")
	img = Image.new("RGBA", code.size, (0, 0, 0, 0))
	size = (int(img.size[0] / 3.5), int(img.size[1] / 3.5))
	pos = (int(img.size[0] * 1.25 / 3.5), int(img.size[1] * 1.25 / 3.5))
	logo = logo.resize(size, Image.Resampling.BILINEAR)
	img.paste(logo, pos)
	img = Image.alpha_composite(code, img)
	print(logo.mode)
	buffered = io.BytesIO()
	img.save(buffered, format="png")
	return 'data:image/png;base64,' + base64.b64encode(buffered.getvalue()).decode("utf-8")
