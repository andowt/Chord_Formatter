
"""

Chord Formatter (c) Andrew West 2022

Software to resize and format PDF chord charts

"""

#--------------------------------------------------------------

import pdfplumber
import sys
import os

from ui import Ui


#--------------------------------------------------------------

def getFileNameArg():

    if len(sys.argv[1:]) != 1:
        print("Failed! - Please supply only one arg")
        exit(1)
    if not(os.path.exists(sys.argv[1])):
        print("Failed! - File does not exits")

    return sys.argv[1]

#--------------------------------------------------------------

def extractLines(filename):

    lines = []
    with pdfplumber.open(filename) as pdf:    
        pages = pdf.pages
        for i,pg in enumerate(pages):
            page = pdf.pages[i]
            text = page.extract_text(layout=True, x_density=5, y_density=13,)
            lines.append(text)
            #print(text) 
    return lines


#--------------------------------------------------------------

def main():
    
    ui = Ui()
    pdf_fn = ui.getFilename()
    lines = extractLines(pdf_fn)
    text_content = ""
    for line in lines:
        text_content+=line
        #print(line)
    ui.showEditorScreen(text_content)
 

#--------------------------------------------------------------


if __name__ == "__main__":
    main()

#--------------------------------------------------------------