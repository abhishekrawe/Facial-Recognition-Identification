from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

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

        title_lbl=Label(bg_img,text="Student Management System" , font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\jsx.png")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)
        
        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column = 0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department" , "Computer ", "IT", "Civil" , "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column = 1, padx=2, pady=10, sticky=W)
        
        
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column = 2,padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="read only")
        course_combo["values"]=("Select Course" , "FE ", "SE", "TE" , "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column = 3, padx=2, pady=10, sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column = 0,padx=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="read only")
        year_combo["values"]=("Select Year" , "2020-21", "2021-22", "2021-23" , "2021-24")
        year_combo.current(0)
        year_combo.grid(row=1,column = 1, padx=2, pady=10, sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column = 2,padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester" , "Semester-1","Semester-2","Semester-3","Semester-4","Semester-5", "Semester-6","Semester-7","Semester-8" )
        semester_combo.current(0)
        semester_combo.grid(row=1,column = 3, padx=2, pady=10, sticky=W)
        
        

        #Class Student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        #student id
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column = 0,padx=10,pady=5, sticky=W)
        
        studentId_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)


        # student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg= "white")
        studentName_label.grid(row=0,column = 2,padx=10,pady=5, sticky=W)
        
        studentId_entry =ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0,column=3,padx=10,pady=5, sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"), bg= "white")
        class_div_label.grid(row=1,column = 0,padx=10, pady=5, sticky=W)
        
        class_div_entry =ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No 
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"), bg = "white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender 
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"), bg = "white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Roll No 
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"), bg = "white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"), bg = "white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"), bg = "white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"), bg = "white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        

        # Teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"), bg = "white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        
        # radiob utton
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample " , value = "Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,text="No Photo Sample", value="yes")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)





        

        
        
        
        
        
        
        
        
        
        
        #Right label frame 

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=780, y=10, width=760, height=580)

        img_right=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\GULP.png")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
       

        # =============Search System==================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Bar System", font=("times new roman",12,"bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"), bg = "red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select" , "Roll_No","Phone_No" )
        search_combo.current(0)
        search_combo.grid(row=0,column = 1, padx=2, pady=10, sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()