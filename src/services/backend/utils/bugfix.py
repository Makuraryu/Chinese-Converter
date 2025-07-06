def isblank(input:str):
    input = input.strip()
    if input == "":
        return 1
    else:
        return 0

if __name__== "__main__":
	print(isblank(""))