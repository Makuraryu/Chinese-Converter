import fitz
from io import BytesIO
from PIL import Image

def pdf2stream(pdf_stream, zoom: float):
    doc = fitz.open(stream=pdf_stream.read(), filetype="pdf")
    streams = []
    for page in doc:
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img_stream = BytesIO(pix.tobytes("png"))
        img_stream.seek(0)
        streams.append(img_stream)
    return streams

def img2stream(image_streams):
    doc = fitz.open()
    for img_stream in image_streams:
        img_stream.seek(0)
        img = Image.open(img_stream).convert("RGB")
        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        pix = fitz.Pixmap(buf.read())
        rect = fitz.Rect(0, 0, pix.width, pix.height)
        page = doc.new_page(width=pix.width, height=pix.height)
        page.insert_image(rect, pixmap=pix)

    pdf_stream = BytesIO()
    doc.save(pdf_stream)
    pdf_stream.seek(0)
    return pdf_stream