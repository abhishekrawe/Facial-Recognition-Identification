from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


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





        #Bg Image
        img3=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\images.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE" , font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # student button
        img4=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100,width =220 , height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300,width =220 , height=40)


        # Detect face button
        img5=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2")
        b1.place(x=630, y=100,width =220 , height=220)

        b1_1=Button(bg_img,text="Face Detector" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=630, y=300,width =220 , height=40)



        # Attendenc face button
        img6=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand2")
        b1.place(x=1100, y=100,width =220 , height=220)

        b1_1=Button(bg_img,text="Attendance" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300,width =220 , height=40)


        # Train face button
        img7=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7, cursor="hand2")
        b1.place(x=200, y=380,width =220 , height=220)

        b1_1=Button(bg_img,text="Train Data" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=580,width =220 , height=40)

        # Photos face button
        img8=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380,width =220 , height=220)

        b1_1=Button(bg_img,text="Train Data" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=580,width =220 , height=40)



        # Photos face button
        img9=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2")
        b1.place(x=630, y=380,width =220 , height=220)

        b1_1=Button(bg_img,text="Photo" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=630, y=580,width =220 , height=40)


        # exit button
        img10=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10, cursor="hand2")
        b1.place(x=1100, y=380,width =220 , height=220)

        b1_1=Button(bg_img,text="exit button" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=580,width =220 , height=40)


    #======================================Function Buttons==========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)




























if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
