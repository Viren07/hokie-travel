"""Makes a QR code that opens the hosted prototype.
Usage: python3 make_qr.py https://viren07.github.io/hokie-travel/   ->  writes qr-code.png
Needs: pip install "qrcode[pil]" """
import sys, qrcode
from PIL import Image, ImageDraw, ImageFont
url = sys.argv[1] if len(sys.argv) > 1 else "https://viren07.github.io/hokie-travel/"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=4)
qr.add_data(url); qr.make(fit=True)
code = qr.make_image(fill_color="#7b1c1c", back_color="white").convert("RGB")
W, H = code.size[0], code.size[1] + 120
out = Image.new("RGB", (W, H), "white"); out.paste(code, (0, 0))
d = ImageDraw.Draw(out)
def font(sz):
    for f in ["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf"]:
        try: return ImageFont.truetype(f, sz)
        except OSError: pass
    return ImageFont.load_default()
for text, y, f, col in [("Scan to try Hokie Travel", code.size[1] - 10, font(40), "#111"),
                        (url.replace("https://", ""), code.size[1] + 50, font(24), "#555")]:
    w = d.textlength(text, font=f); d.text(((W - w) / 2, y), text, font=f, fill=col)
out.save("qr-code.png"); print("Wrote qr-code.png for", url)
