from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
    
        
        #First Image
        img=Image.open(r"college_images\jsx.png")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)




        #Second Image
        img1=Image.open(r"college_images\memories.png")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0 ,width=800,height=200)

       

        #bg Image
        img3=Image.open(r"college_images\es6.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200 ,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendence Management System ",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left=Image.open(r"college_images\jsx.png")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #attendence id 
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column = 0,padx=10,pady=5, sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)


        # Neam 
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)


        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
       
        # date 
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        # Department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        # Time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)


        # Date
        dateLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # Time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)


        # Time
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update ",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        

        #Right label frame 

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Attendence Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)


        # =========================scroll bar table================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id",text="Attendence ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")

        self.AttendaceReportTable["show"]="headings"

        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)
       
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)








if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()