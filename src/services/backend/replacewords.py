from .utils.ocr import ocr,combine_chars,getwords,wordsin
from .utils.transform import transform
from .utils.draw import replace,buffer

def imagereplace(ocrKey:str,dsKey:str,lang:int,img):
    targetlang = 1 - lang
    rawocr = ocr(ocrKey,img,lang)
    combined = combine_chars(rawocr)
    words = getwords(rawocr)
    transcom = transform(dsKey,combined,targetlang)
    data = wordsin(transcom,words)
    replaced = replace(img,data)
    buf = buffer(replaced)
    return buf

    