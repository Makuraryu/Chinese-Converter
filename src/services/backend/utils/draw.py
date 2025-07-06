from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import io

ROOT = Path(__file__).parent.resolve()
FONT = ROOT/"font.ttc"

def pickbgcolor(img, x:int, y:int):
    r, g, b = img.getpixel((x, y))
    return (r, g, b)

def textcolor(rgb:tuple):
    r, g, b = rgb
    # Simple heuristic to determine if the text should be black or white
    if (r + g + b) / 3 < 128:  # If the average color is dark
        return 'white'
    else:
        return 'black'

def replace(img,data):
    #img = Image.open(img)
    img = Image.open(img).convert("RGB")
    draw = ImageDraw.Draw(img)

    for datum in data:
        left = datum['left']
        top = datum['top']
        width = datum['width']
        height = datum['height']
        text = datum['char']
        try:
            font = ImageFont.truetype(FONT, size=height)
        except:
            print("no font")
            font = ImageFont.load_default()
        curcolor = pickbgcolor(img, left, top)
        txtcolor = textcolor(curcolor)
        draw.rectangle([left, top, left + width, top+height], fill=curcolor)
        draw.text((left, top-0.25*height), text, fill=txtcolor, font=font)
    return img

def buffer(img):
    buf = io.BytesIO()
    img.save(buf,"PNG")
    buf.seek(0)
    return buf

if __name__ == "__main__":
    data = [{'char': '接', 'left': 58.0, 'top': 35.0, 'width': 14.0, 'height': 12.0}, {'char': '囗', 'left': 73.0, 'top': 35.0, 'width': 12.0, 'height': 12.0}, {'char': '文', 'left': 86.0, 'top': 35.0, 'width': 14.0, 'height': 12.0}, {'char': '档', 'left': 100.0, 'top': 35.0, 'width': 14.0, 'height': 12.0}, {'char': '@', 'left': 30.0, 'top': 77.0, 'width': 15.0, 'height': 15.0}, {'char': '堂', 'left': 59.0, 'top': 79.0, 'width': 13.0, 'height': 12.0}, {'char': '见', 'left': 72.0, 'top': 79.0, 'width': 14.0, 'height': 12.0}, {'char': '问', 'left': 87.0, 'top': 79.0, 'width': 12.0, 'height': 12.0}, {'char': '题', 'left': 100.0, 'top': 79.0, 'width': 14.0, 'height': 12.0}, {'char': '产', 'left': 58.0, 'top': 123.0, 'width': 14.0, 'height': 12.0}, {'char': '品', 'left': 73.0, 'top': 123.0, 'width': 12.0, 'height': 12.0}, {'char': '定', 'left': 86.0, 'top': 123.0, 'width': 15.0, 'height': 12.0}, {'char': '价', 'left': 101.0, 'top': 123.0, 'width': 13.0, 'height': 12.0}, {'char': '实', 'left': 58.0, 'top': 167.0, 'width': 14.0, 'height': 12.0}, {'char': '甲', 'left': 73.0, 'top': 167.0, 'width': 12.0, 'height': 12.0}, {'char': '成', 'left': 101.0, 'top': 167.0, 'width': 13.0, 'height': 12.0}, {'char': '联', 'left': 58.0, 'top': 211.0, 'width': 14.0, 'height': 12.0}, {'char': '系', 'left': 73.0, 'top': 211.0, 'width': 13.0, 'height': 12.0}, {'char': '我', 'left': 86.0, 'top': 211.0, 'width': 14.0, 'height': 12.0}, {'char': '们', 'left': 100.0, 'top': 211.0, 'width': 13.0, 'height': 12.0}]
    img = replace("input.png",data)
    img.save("out.png")