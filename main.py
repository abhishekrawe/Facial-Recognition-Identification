from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognition_System:
    def __init__(self,root):  
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        

        #First Image
        img=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\jsx.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)




        #Second Image
        img1=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\memories.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)





        #Third Image
        img2=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\js.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        









if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
