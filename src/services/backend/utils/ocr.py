import requests
def ocr(apiKey:str,img,lang:int):
    if lang == 0:
        ch = 'chs'#简体中文
    else:
        ch = 'cht'#繁体中文
    URL = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': apiKey,
        'language': ch,
        'isOverlayRequired': True,
    }
    files = {'image': ("input.png", img, 'image/png')}
    #files = {'image': (img.filename, img.stream, img.mimetype)}
    #files = {'file': open(img, 'rb')}

    r = requests.post(URL, data=payload, files=files)
    result = r.json()

    try:
        lines = result['ParsedResults'][0]['TextOverlay']['Lines']
    except:
        print("OCR raw result:", result)
        return 1

    extracted = []

    for line in lines:
        line_text = line['LineText']
        words = [{
            'char': word['WordText'],
            'left': word['Left'],
            'top': word['Top'],
            'width': word['Width'],
            'height': word['Height']
        } for word in line['Words']]
        extracted.append({
            'line_text': line_text,
            'words': words
        })

    return extracted

def combine_chars(data):
    all_chars = []
    for line in data:
        for word in line['words']:
            all_chars.append(word['char'])
    return ''.join(all_chars)

def getwords(data):
    result = []
    for line in data:
        for word in line['words']:
            result.append(word)
    return result

def wordsin(texts,words):
    i = 0
    replaced = []
    for word in words:
        word['char'] = texts[i]
        replaced.append(word)
        i = i + 1
    return replaced
        

if __name__ == "__main__":
    ocrkey = 'K88456352888957'
    input = 'input.png'
    ocred = ocr(ocrkey,input,0)
    combined = combine_chars(ocred)
    words = getwords(ocred)
    replaced = wordsin(combined,words)
    print(replaced)