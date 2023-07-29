import os
import sys
from translate import Translator

def file_translation(input, output, output_language):
    with open(input, "r") as f:
        contents = f.read()

    translator = Translator(to_lang=output_language)
    translated_text = translator.translate(contents)
    with open(output,"w") as f:
        f.write(translated_text)

if __name__ == "__main__":
    output_language = input("Enter the output language: ")
    input = "input.txt"
    output = "output.txt"
    if (os.path.isfile(input)):
        file_translation(input, output, output_language)
    else:
        print("create a input.txt file with some text")
        sys.exit()

