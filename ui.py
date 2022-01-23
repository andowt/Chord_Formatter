import tkinter
from tkinter import filedialog
import os

class Ui(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('MATE - Chord Formatter')
        self.root.geometry('600x900')
        self.root.withdraw()

    def getFilename(self):
        currdir = os.getcwd()
        self.pdf_fn = filedialog.askopenfilename(parent=self.root, initialdir=currdir, title='Please select pdf file')
        if len(self.pdf_fn) > 0:
            print(f"You chose {self.pdf_fn}")
        return self.pdf_fn

    def showEditorScreen(self, message):
        self.text_box = tkinter.Text(
            self.root,
            height=500,
            width=800
            )
        self.button = tkinter.Button(self.root, text="Save", command=self.saveCallback)
        self.button.pack(expand=True)
        self.text_box.pack(expand=True)
        self.text_box.insert('end', message)
        self.text_box.config(state='normal')
        self.root.deiconify()
        self.root.mainloop()
    
    def saveCallback(self):
        input = self.text_box.get("1.0",'end-1c')
        print(input)
        self.root.destroy() # Resume program flow


