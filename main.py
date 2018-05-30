from translators import *
import sys

if (__name__ == "__main__" and len(sys.argv) == 1):
    phraseToTranslate = input()
elif (sys.argv[1] != ""):
    phraseToTranslate = sys.argv[1]
else:
    print("Error reading input")    

phraseTranslated = Translator(phraseToTranslate).translate()

#.split()
print(phraseTranslated)