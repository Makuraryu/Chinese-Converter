from .utils.ocr import ocr,combine_chars,getwords,wordsin
from .utils.transform import transform
from .utils.draw import replace,buffer
from .utils.imgpdf import pdf2stream,img2stream

def pdfreplace(ocrKey:str,dsKey:str,lang:int,pdf):
    targetlang = 1 - lang
    replaceds = []
    imgs = pdf2stream(pdf, 1)
    for img in imgs:
        targetlang = 1 - lang
        rawocr = ocr(ocrKey,img,lang)
        combined = combine_chars(rawocr)
        words = getwords(rawocr)
        transcom = transform(dsKey,combined,targetlang)
        data = wordsin(transcom,words)
        replaced = replace(img,data)
        buf = buffer(replaced)
        replaceds.append(buf)
    res = img2stream(replaceds)
    return res