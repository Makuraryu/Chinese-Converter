from flask import Flask,request,send_file,send_from_directory
from .transformation import transformation
from .replacewords import imagereplace
from pathlib import Path
from .config import ocrkey,apikey
from .replacepdf import pdfreplace
ROOT = Path(__file__).parent.resolve()
FRONT = ROOT.parent/"frontend"
STYLE = FRONT/"style"
INDEX = FRONT/"index.html"
TRANS = FRONT/"transformation.html"
IMAGE = FRONT/"image.html"
PDF = FRONT/"pdf.html"



app = Flask(__name__)



@app.route('/')
def index():
    return open(INDEX, encoding='utf-8').read()

@app.route('/style/<path:filename>')
def css(filename):
    return send_from_directory(STYLE, filename)


@app.route('/transformation')
def translating():
    return open(TRANS, encoding='utf-8').read()

@app.route('/image')
def image():
    return open(IMAGE, encoding='utf-8').read()

@app.route('/pdf')
def pdf():
    return open(PDF, encoding ='utf-8').read()

@app.route('/api/transform',methods=['POST'])
def trans():
    data = request.json
    return transformation(apikey,data["input"],data["ch"])    

@app.route('/api/image',methods=['POST'])
def img():
    ch = request.form.get("number")
    image = request.files.get("image")
    if not image:
        return "Missing image", 400
    chint = int(ch) if ch else 0
    dealed = imagereplace(ocrkey,apikey,chint,image.stream)
    return send_file(dealed, mimetype="image/png")

@app.route('/api/pdf',methods=['POST'])
def p():
    ch = request.form.get("number")
    pdf = request.files.get("pdf")
    if not pdf:
        return "Missing pdf", 400
    chint = int(ch) if ch else 0
    dealed = pdfreplace(ocrkey,apikey,chint,pdf.stream)
    return send_file(dealed, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)