#! python3

import docx

def getText(filename):
    doc = docx.Document(filename)

    fileText = []
    for para in doc.paragraphs:
        fileText.append(para.text)
    return  '\n'.join(fileText)

