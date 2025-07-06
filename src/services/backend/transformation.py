from .utils.transform import transform
from .utils.bugfix import isblank

def transformation(apiKey:str,input:str,ch:int):
    if isblank(input)== 1:
        return "Input is blank"
    return transform(apiKey,input,ch)