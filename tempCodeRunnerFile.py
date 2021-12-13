        # exit button
        img8=Image.open(r"C:\Users\HP\Desktop\facerecognisationsystem\college_images\search.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=380,width =220 , height=220)

        b1_1=Button(bg_img,text="Exit" , cursor="hand2" ,  font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=580,width =220 , height=40)