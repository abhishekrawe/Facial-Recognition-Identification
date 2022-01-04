#buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman", 13 , "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)