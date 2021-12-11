from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognition_System:
    def __init__(self,root):  
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")




if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
