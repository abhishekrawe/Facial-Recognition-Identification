from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognition_System:
    def __init__(self,root):  
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\jsx.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)






if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
