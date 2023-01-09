from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter
from SAGEAIbot import sage

class Staff:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x730+0+0")
        self.root.title("Staff Registration")

        # =======variables===========

        self.var_dept=StringVar()
        self.var_rgstrn=StringVar()
        self.var_dor=StringVar()
        self.var_hrn=StringVar()
        self.var_staffname=StringVar()
        self.var_age=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_adhaarnumber=StringVar()
        self.var_bloodgroup=StringVar()
        self.var_pannumber=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()

        imgsr=Image.open(r"D:\IPProjectFinal\backgrounds\26365.jpg")
        imgsr=imgsr.resize((1300,735),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(imgsr)

        prbgimg=Label(self.root,image=self.photoimg)
        prbgimg.place(x=0,y=0,width=1300,height=735)

        title=Label(prbgimg,text="Staff Registration",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        title.place(x=0,y=10,width=1310,height=60)
        
        #=========gui background==============
        main_frame=Frame(prbgimg,bd=2,bg="powder blue")
        main_frame.place(x=50,y=90,width=1170,height=620)
        #==========left frame==================
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Staff Directory",font=("times new roman",12,"bold",))
        left_frame.place(x=0,y=10,width=570,height=600)

        imgsb=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imgsb=imgsb.resize((600,100),Image.ANTIALIAS)
        self.photoimg31=ImageTk.PhotoImage(imgsb)

        sframe=Label(self.root,image=self.photoimg31)
        sframe.place(x=90,y=130,width=500,height=70)
        #frame1
        frame_1=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Staff Record",font=("times new roman",12,"bold",))
        frame_1.place(x=0,y=90,width=565,height=110)
        #department
        dept_label=Label(frame_1,text="Department:",font=("times new roman",12,"bold"),fg="black")
        dept_label.grid(row=0,column=0)

        dept_combo=ttk.Combobox(frame_1,textvariable=self.var_dept,font=("times new roman",12,"bold"),state="readonly",width=14)
        dept_combo["values"]=("Select Dept","Doctor","Nurse","Intern","Security","EmergencyRescue","IT operator")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=5)
        # registration no.
        rgstrn_label=Label(frame_1,text="Registration Number:",font=("times new roman",12,"bold"),fg="black")
        rgstrn_label.grid(row=0,column=2)

        rgstrn_combo=ttk.Entry(frame_1,textvariable=self.var_rgstrn,font=("times new roman",12,"bold"),width=16)
        rgstrn_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)
        # registration date
        dor_label=Label(frame_1,text="Registration Date:",font=("times new roman",12,"bold"),fg="black")
        dor_label.grid(row=1,column=0)

        dor_combo=ttk.Entry(frame_1,textvariable=self.var_dor,font=("times new roman",12,"bold"),width=16)
        dor_combo.grid(row=1,column=1,padx=2,pady=15,sticky=W)
        # registration no given by hospital
        hrn_label=Label(frame_1,text="Hospital RegisNum:",font=("times new roman",12,"bold"),fg="black")
        hrn_label.grid(row=1,column=2)

        hrn_combo=ttk.Entry(frame_1,textvariable=self.var_hrn,font=("times new roman",12,"bold"),width=16)
        hrn_combo.grid(row=1,column=3,padx=2,pady=4,sticky=W)
        #frame2
        frame_2=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Patient Data",font=("times new roman",12,"bold",))
        frame_2.place(x=0,y=200,width=565,height=377)
        # name
        staffname_label=Label(frame_2,text="Staff Name:",font=("times new roman",12,"bold"),fg="black")
        staffname_label.grid(row=0,column=0,padx=5,pady=5)
        
        staffname_entry=ttk.Entry(frame_2,textvariable=self.var_staffname,font=("times new roman",12,"bold"),width=18)
        staffname_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        # age
        age_label=Label(frame_2,text="Age:",font=("times new roman",12,"bold"),fg="black")
        age_label.grid(row=0,column=2,padx=5,pady=5)
        
        age_entry=ttk.Entry(frame_2,textvariable=self.var_age,font=("times new roman",12,"bold"),width=18)
        age_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Date of birth
        dob_label=Label(frame_2,text="Date of Birth:",font=("times new roman",12,"bold"),fg="black")
        dob_label.grid(row=1,column=0,padx=5,pady=5)
        
        dob_entry=ttk.Entry(frame_2,textvariable=self.var_dob,font=("times new roman",12,"bold"),width=18)
        dob_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    # gender
        gender_label=Label(frame_2,text="Gender:",font=("times new roman",12,"bold"),fg="black")
        gender_label.grid(row=1,column=2,padx=5,pady=5)

        gender_combo=ttk.Combobox(frame_2,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=5)
    
    # Adhaar Number
        adhaarnumber_label=Label(frame_2,text="Adhaar Number:",font=("times new roman",12,"bold"),fg="black")
        adhaarnumber_label.grid(row=2,column=0,padx=5,pady=5)

        adhaarnumber_entry=ttk.Entry(frame_2,textvariable=self.var_adhaarnumber,font=("times new roman",12,"bold"),width=18)
        adhaarnumber_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    # bloodgroup
        bloodgroup_label=Label(frame_2,text="Blood Group:",font=("times new roman",12,"bold"),fg="black")
        bloodgroup_label.grid(row=2,column=2,padx=5,pady=5)

        bloodgroup_combo=ttk.Combobox(frame_2,textvariable=self.var_bloodgroup,font=("times new roman",12,"bold"),state="readonly",width=16)
        bloodgroup_combo["values"]=("Select Blood Group","A+","A-","B+","B-","O+","O-","AB+","AB-")
        bloodgroup_combo.current(0)
        bloodgroup_combo.grid(row=2,column=3,padx=5,pady=5)


    # Pan number
        pannumber_label=Label(frame_2,text="PAN Number:",font=("times new roman",12,"bold"),fg="black")
        pannumber_label.grid(row=3,column=0,padx=5,pady=5)

        pannumber_entry=ttk.Entry(frame_2,textvariable=self.var_pannumber,font=("times new roman",12,"bold"),width=18)
        pannumber_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    # Email ID
        email_label=Label(frame_2,text="Email ID",font=("times new roman",12,"bold"),fg="black")
        email_label.grid(row=3,column=2,padx=5,pady=5)

        email_entry=ttk.Entry(frame_2,textvariable=self.var_email,font=("times new roman",12,"bold"),width=18)
        email_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

    # Address
        address_label=Label(frame_2,text="Address",font=("times new roman",12,"bold"),fg="black")
        address_label.grid(row=4,column=0,padx=5,pady=5)

        address_entry=ttk.Entry(frame_2,textvariable=self.var_address,font=("times new roman",12,"bold"),width=18)
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    # phonenumber
        phone_label=Label(frame_2,text="Phone No.:",font=("times new roman",12,"bold"),fg="black")
        phone_label.grid(row=4,column=2,padx=5,pady=5)
        
        phone_entry=ttk.Entry(frame_2,textvariable=self.var_phone,font=("times new roman",12,"bold"),width=18)
        phone_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
    
    # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(frame_2,variable=self.var_radio1,text="Take Image",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(frame_2,variable=self.var_radio1,text="No Image",value="No")
        radiobtn2.grid(row=5,column=1)

    # button frame1
        btn_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        btn_frame.place(x=0,y=495,width=565,height=40)

    # button frame2
        btn_frame1=LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        btn_frame1.place(x=0,y=535,width=565,height=40)

    # save
        savebtn1=Button(btn_frame,text="Save",command=self.add_data,width=11,font=("times new roman",16,"bold"),bg="blue",fg="white")
        savebtn1.grid(row=0,column=0)

    # update
        Updatebtn1=Button(btn_frame,text="Update",command=self.update_data,width=11,font=("times new roman",16,"bold"),bg="blue",fg="white")
        Updatebtn1.grid(row=0,column=1)

    # delete
        deletebtn1=Button(btn_frame,text="Delete",command=self.delete_data,width=11,font=("times new roman",16,"bold"),bg="blue",fg="white")
        deletebtn1.grid(row=0,column=2)

    # reset
        resetbtn1=Button(btn_frame,text="Reset",command=self.reset_data,width=11,font=("times new roman",16,"bold"),bg="blue",fg="white")
        resetbtn1.grid(row=0,column=3)

    # take photo
        takephtobtn1=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=22,font=("times new roman",16,"bold"),bg="blue",fg="white")
        takephtobtn1.grid(row=0,column=0)

    # update photo
        updatephtobtn1=Button(btn_frame1,text="Update Photo",command=self.generate_dataset,width=23,font=("times new roman",16,"bold"),bg="blue",fg="white")
        updatephtobtn1.grid(row=0,column=1)
        
    # extra
        imgbttn2=Image.open(r"D:\IPProjectFinal\icons\chatbotbttn.png")
        imgbttn2=imgbttn2.resize((50,50),Image.ANTIALIAS)
        self.photoimgbt2=ImageTk.PhotoImage(imgbttn2)

        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\exitbttn.png")
        imgbttn1=imgbttn1.resize((50,50),Image.ANTIALIAS)
        self.photoimgexit=ImageTk.PhotoImage(imgbttn1)
        exitbttn = Button(title,image=self.photoimgexit,command=self.Exit,cursor="hand2",bg="white",width=0,height=60,activebackground="white")
        exitbttn.place(x=1150, y=0)
        sagebtn1=Button(title,command=self.chatbot,image=self.photoimgbt2,bg="white",activebackground="white")
        sagebtn1.place(x=1090,y=0,width=55,height=55)

        #===========right frame===================
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Report",font=("times new roman",12,"bold"))
        right_frame.place(x=600,y=10,width=570,height=600)

        imgsb1=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imgsb1=imgsb1.resize((600,100),Image.ANTIALIAS)
        self.photoimg32=ImageTk.PhotoImage(imgsb)

        s2frame=Label(self.root,image=self.photoimg32)
        s2frame.place(x=690,y=130,width=500,height=70)

        title=Label(right_frame,text="*Carefully select hospital resgistration number",font=("times new roman",15,"bold"),bg="light blue",fg="green")
        title.place(x=0,y=90,width=565,height=30)
        title=Label(right_frame,text="*Please fill the deatils carefully",font=("times new roman",15,"bold"),bg="light blue",fg="green")
        title.place(x=0,y=120,width=565,height=30)

        #frame
        frame_4=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Data:",font=("times new roman",12,"bold"))
        frame_4.place(x=0,y=150,width=565,height=425)   
    #data box   
        scroll_x=ttk.Scrollbar(frame_4,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_4,orient=VERTICAL)

        self.staff_records=ttk.Treeview(frame_4,columns=("dept","rgstrn","dor","hrn","staffname","age","dob","gender","adhaarnumber","bloodgroup","pannumber","email","address","phone","radio1"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_records.xview)
        scroll_y.config(command=self.staff_records.yview)
        
        self.staff_records.heading("dept",text="Department")
        self.staff_records.heading("rgstrn",text="Registration Number")
        self.staff_records.heading("dor",text="Registration Date")
        self.staff_records.heading("hrn",text="Hospital Registration Number")
        self.staff_records.heading("staffname",text="Staff Name")
        self.staff_records.heading("age",text="Age")
        self.staff_records.heading("dob",text="Date of Birth")
        self.staff_records.heading("gender",text="Gender")
        self.staff_records.heading("adhaarnumber",text="Adhaar Number")
        self.staff_records.heading("bloodgroup",text="Blood Group")
        self.staff_records.heading("pannumber",text="PAN Number")
        self.staff_records.heading("email",text="Email")
        self.staff_records.heading("address",text="Address")
        self.staff_records.heading("phone",text="Phone")
        self.staff_records.heading("radio1",text="Photo")
        self.staff_records["show"]="headings"

        self.staff_records.column("dept",width=100)
        self.staff_records.column("rgstrn",width=120)
        self.staff_records.column("dor",width=100)
        self.staff_records.column("hrn",width=120)
        self.staff_records.column("staffname",width=100)
        self.staff_records.column("age",width=100)
        self.staff_records.column("dob",width=100)
        self.staff_records.column("gender",width=100)
        self.staff_records.column("adhaarnumber",width=100)
        self.staff_records.column("bloodgroup",width=100)
        self.staff_records.column("pannumber",width=100)
        self.staff_records.column("email",width=100)
        self.staff_records.column("address",width=100)
        self.staff_records.column("phone",width=100)
        self.staff_records.column("radio1",width=100)

        self.staff_records.pack(fill=BOTH,expand=1)
        self.staff_records.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dept.get()=="Select Dept" or self.var_rgstrn.get()=="" or self.var_staffname.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into staff_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.var_dept.get(),
                                                                                                         self.var_rgstrn.get(),
                                                                                                         self.var_dor.get(),
                                                                                                         self.var_hrn.get(),
                                                                                                         self.var_staffname.get(),
                                                                                                         self.var_age.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_adhaarnumber.get(),
                                                                                                         self.var_bloodgroup.get(),
                                                                                                         self.var_pannumber.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_radio1.get()

                                                                                                ))
                conn.commit()
                #self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Staff Data Added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#===================fetch data========================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from staff_data")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.staff_records.delete(*self.staff_records.get_children())
            for i in data:
                self.staff_records.insert("",END,values=i)
            conn.commit()
        conn.close()

#==================update data========================= 
    def get_cursor(self,event=""):
        cursor_focus=self.staff_records.focus()
        content=self.staff_records.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_rgstrn.set(data[1]),
        self.var_dor.set(data[2]),
        self.var_hrn.set(data[3]),
        self.var_staffname.set(data[4]),
        self.var_age.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_adhaarnumber.set(data[8]),
        self.var_bloodgroup.set(data[9]),
        self.var_pannumber.set(data[10]),
        self.var_email.set(data[11]),
        self.var_address.set(data[12]),
        self.var_phone.set(data[13]),
        self.var_radio1.set(data[14])

#=========update function=====================
    def update_data(self):
        if self.var_dept.get()=="Select Dept" or self.var_rgstrn.get()=="" or self.var_staffname.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Updatedata=messagebox.askyesno("Updatedata","Do you want to update this Staff info",parent=self.root)
                if Updatedata>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update staff_data set dept=%s,dor=%s,hrn=%s,staffname=%s,age=%s,dob=%s,gender=%s,adhaarnumber=%s,bloodgroup=%s,pannumber=%s,email=%s,address=%s,phone=%s,photo=%s where rgstrn=%s",(

                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                            self.var_dor.get(),
                                                                                                                                                            self.var_hrn.get(),
                                                                                                                                                            self.var_staffname.get(),
                                                                                                                                                            self.var_age.get(),
                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_adhaarnumber.get(),
                                                                                                                                                            self.var_bloodgroup.get(),
                                                                                                                                                            self.var_pannumber.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_rgstrn.get()

                                                                                                                                                    ))
                else:
                    if not Updatedata:
                        return
                messagebox.showinfo("Success","Staff details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#============delete function=================
    def delete_data(self):
        if self.var_rgstrn.get()=="":
            messagebox.showerror("Error","Staff registration number is required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Staff Data Delete","Are you the certified operator to use this function",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                    my_cursor=conn.cursor()
                    sql="delete from staff_data where rgstrn=%s"
                    val=(self.var_rgstrn.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted staff",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#====================reset function=================
    def reset_data(self):
        self.var_dept.set("Select Dept")
        self.var_rgstrn.set("")
        self.var_dor.set("")
        self.var_hrn.set("")
        self.var_staffname.set("")
        self.var_age.set("")
        self.var_dob.set("")
        self.var_gender.set("Select Gender")
        self.var_adhaarnumber.set("")
        self.var_bloodgroup.set("Select Blood Group")
        self.var_pannumber.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_radio1.set("")
#==================dataset for images===========================
    def generate_dataset(self):
        if self.var_dept.get()=="Select Dept" or self.var_rgstrn.get()=="" or self.var_staffname.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from staff_data")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update staff_data set dept=%s,dor=%s,hrn=%s,staffname=%s,age=%s,dob=%s,gender=%s,adhaarnumber=%s,bloodgroup=%s,pannumber=%s,email=%s,address=%s,phone=%s,photo=%s where rgstrn=%s",(
                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                            self.var_dor.get(),
                                                                                                                                                            self.var_hrn.get(),
                                                                                                                                                            self.var_staffname.get(),
                                                                                                                                                            self.var_age.get(),
                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_adhaarnumber.get(),
                                                                                                                                                            self.var_bloodgroup.get(),
                                                                                                                                                            self.var_pannumber.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_rgstrn.get()==id+1
                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # load predifined data
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="datastaff/staffname."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Are you sure you want to exit staff registration tab?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return
    def chatbot(self):
        self.new_window2=Toplevel(self.root)
        self.app=sage(self.new_window2)


if __name__ =="__main__":
    root=Tk()
    obj=Staff(root)
    root.mainloop()