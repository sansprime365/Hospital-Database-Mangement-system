from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter
from SAGEAIbot import sage

class Patient:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1310x730+0+0")
        self.root.title("Patient Registration")

        # =======variables===========

        self.var_agegroup=StringVar()
        self.var_profession=StringVar()
        self.var_healthproblem=StringVar()
        self.var_room=StringVar()
        self.var_patientname=StringVar()
        self.var_registration=StringVar()
        self.var_bp=StringVar()
        self.var_gender=StringVar()
        self.var_weight=StringVar()
        self.var_height=StringVar()
        self.var_oxygen=StringVar()
        self.var_heart=StringVar()
        self.var_dor=StringVar()
        self.var_phone=StringVar()

        # ========emergency===========
        self.var_roomno=StringVar()
        self.var_severe=StringVar()

        imgpr1=Image.open(r"D:\IPProjectFinal\backgrounds\26365.jpg")
        imgpr1=imgpr1.resize((1310,735),Image.ANTIALIAS)
        self.photoimgprbg1=ImageTk.PhotoImage(imgpr1)

        bgimg1=Label(self.root,image=self.photoimgprbg1)
        bgimg1.place(x=0,y=0,width=1310,height=735)

        title=Label(bgimg1,text="Patient Registration",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        title.place(x=0,y=10,width=1310,height=60)

        #rbutton=Button(text="Return", font=("Arial", 15,"bold"),cursor="hand2")#command=self.homep)
        #rbutton.place(x=750, y=300)
    
    # bg frame
        patientregistration_frame=Frame(bgimg1,bd=2,bg="powder blue")
        patientregistration_frame.place(x=50,y=90,width=1170,height=620)

    # left box
        left_frame=LabelFrame(patientregistration_frame,bd=2,relief=RIDGE,text="Patient Directory",font=("times new roman",12,"bold",))
        left_frame.place(x=0,y=10,width=570,height=600)

        imglb=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imglb=imglb.resize((600,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(imglb)

        lframe=Label(self.root,image=self.photoimg1)
        lframe.place(x=90,y=140,width=500,height=70)

    # in record box
        frame_1=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Patient Record",font=("times new roman",12,"bold",))
        frame_1.place(x=0,y=90,width=565,height=110)
    
    # Age Group

        agegroup_label=Label(frame_1,text="Age Group:",font=("times new roman",12,"bold"),fg="black")
        agegroup_label.grid(row=0,column=0)

        agegroup_combo=ttk.Combobox(frame_1,textvariable=self.var_agegroup,font=("times new roman",12,"bold"),state="readonly",width=18)
        agegroup_combo["values"]=("Select Age Group","New Baby(2months-1year)","Kids(1-10years)","Adolescent(10-19years)","Adults(19-39years)","OlderAdults(39+years)")
        agegroup_combo.current(0)
        agegroup_combo.grid(row=0,column=1,padx=2)

    # profession

        profession_label=Label(frame_1,text="Profession:",font=("times new roman",12,"bold"),fg="black")
        profession_label.grid(row=0,column=2)

        profession_combo=ttk.Combobox(frame_1,textvariable=self.var_profession,font=("times new roman",12,"bold"),state="readonly",width=18)
        profession_combo["values"]=("Select Profession","Student","Working","Retired")
        profession_combo.current(0)
        profession_combo.grid(row=0,column=3,padx=2,pady=10)

    # Health problems

        healthproblem_label=Label(frame_1,text="Health Issue:",font=("times new roman",12,"bold"),fg="black")
        healthproblem_label.grid(row=1,column=0)

        healthproblem_combo=ttk.Combobox(frame_1,textvariable=self.var_healthproblem,font=("times new roman",12,"bold"),state="readonly",width=18)
        healthproblem_combo["values"]=("Select Health Issue","allergies","muscular/joints/bone","cancer","child health","diabetes","eyes","blood and immune system","brain and nervous system","chest and lungs","general checkup","cardio issue","skin and nails","mental health")
        healthproblem_combo.current(0)
        healthproblem_combo.grid(row=1,column=1,padx=2)

    # Room No.

        room_label=Label(frame_1,text="Room Issued:",font=("times new roman",12,"bold"),fg="black")
        room_label.grid(row=1,column=2)

        room_combo=ttk.Combobox(frame_1,textvariable=self.var_room,font=("times new roman",12,"bold"),state="readonly",width=18)
        room_combo["values"]=("Select Room","hrn01","hrn02","hrn03","hrn04","hrn05","hrn06","hrn07","hrn08","hrn09","hrn10","hrn11","hrn12")
        room_combo.current(0)
        room_combo.grid(row=1,column=3,padx=2,pady=10)

    # in record box
        frame_2=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Patient Data",font=("times new roman",12,"bold",))
        frame_2.place(x=0,y=200,width=565,height=377)

    # name
        patientname_label=Label(frame_2,text="PatientName:",font=("times new roman",12,"bold"),fg="black")
        patientname_label.grid(row=0,column=0,padx=5,pady=5)
        
        patientname_entry=ttk.Entry(frame_2,textvariable=self.var_patientname,font=("times new roman",12,"bold"),width=18)
        patientname_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    # Patient no.
        registration_label=Label(frame_2,text="Regstrn No.:",font=("times new roman",12,"bold"),fg="black")
        registration_label.grid(row=0,column=2,padx=5,pady=5)
        
        registration_entry=ttk.Entry(frame_2,textvariable=self.var_registration,font=("times new roman",12,"bold"),width=18)
        registration_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    # BP
        bp_label=Label(frame_2,text="BP Rate:",font=("times new roman",12,"bold"),fg="black")
        bp_label.grid(row=1,column=0,padx=5,pady=5)
        
        bp_entry=ttk.Entry(frame_2,textvariable=self.var_bp,font=("times new roman",12,"bold"),width=18)
        bp_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    # gender
        gender_label=Label(frame_2,text="Gender:",font=("times new roman",12,"bold"),fg="black")
        gender_label.grid(row=1,column=2,padx=5,pady=5)

        gender_combo=ttk.Combobox(frame_2,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=5)
    
    # weight
        weight_label=Label(frame_2,text="Weight:",font=("times new roman",12,"bold"),fg="black")
        weight_label.grid(row=2,column=0,padx=5,pady=5)
        
        weight_entry=ttk.Entry(frame_2,textvariable=self.var_weight,font=("times new roman",12,"bold"),width=18)
        weight_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    # height
        height_label=Label(frame_2,text="Height:",font=("times new roman",12,"bold"),fg="black")
        height_label.grid(row=2,column=2,padx=5,pady=5)
        
        height_entry=ttk.Entry(frame_2,textvariable=self.var_height,font=("times new roman",12,"bold"),width=18)
        height_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)


    # Oxygen Rate
        oxygen_label=Label(frame_2,text="Oxygen Rate:",font=("times new roman",12,"bold"),fg="black")
        oxygen_label.grid(row=3,column=0,padx=5,pady=5)
        
        oxygen_entry=ttk.Entry(frame_2,textvariable=self.var_oxygen,font=("times new roman",12,"bold"),width=18)
        oxygen_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    # Heart Rate    
        heart_label=Label(frame_2,text="Heart Rate:",font=("times new roman",12,"bold"),fg="black")
        heart_label.grid(row=3,column=2,padx=5,pady=5)
        
        heart_entry=ttk.Entry(frame_2,textvariable=self.var_heart,font=("times new roman",12,"bold"),width=18)
        heart_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

    # date of enrollment
        dor_label=Label(frame_2,text="Regstrn Date:",font=("times new roman",12,"bold"),fg="black")
        dor_label.grid(row=4,column=0,padx=5,pady=5)
        
        dor_entry=ttk.Entry(frame_2,textvariable=self.var_dor,font=("times new roman",12,"bold"),width=18)
        dor_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

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
        deletebtn1=Button(btn_frame,text="Delete",command=self.delete_data,width=11,font=("times new roman",16,"bold"),bg="blue",fg="white",activebackground="red",activeforeground="white")
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
 
    # right box
        right_frame=LabelFrame(patientregistration_frame,bd=2,relief=RIDGE,text="Report",font=("times new roman",12,"bold",),borderwidth=0)
        right_frame.place(x=600,y=10,width=570,height=600)

        imglb1=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imglb1=imglb1.resize((600,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(imglb1)

        lframe=Label(self.root,image=self.photoimg2)
        lframe.place(x=680,y=140,width=500,height=70)

    # Emergency tab
        frame_3=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Emergency Tab",font=("times new roman",12,"bold"))
        frame_3.place(x=0,y=500,width=565,height=70)

        room_label=Label(frame_3,text="Room Issued:",font=("times new roman",12,"bold"),fg="black")
        room_label.grid(row=0,column=0)

        room_combo=ttk.Combobox(frame_3,textvariable=self.var_roomno,font=("times new roman",12,"bold"),state="readonly",width=9)
        room_combo["values"]=("Select Room","hrn01","hrn02","hrn03","hrn04","hrn05","hrn06","hrn07","hrn08","hrn09","hrn10","hrn11","hrn12")
        room_combo.current(0)
        room_combo.grid(row=0,column=1,padx=2,pady=10)

        threat_label=Label(frame_3,text="Severity:",font=("times new roman",12,"bold"),fg="black")
        threat_label.grid(row=0,column=3)

        threat_combo=ttk.Combobox(frame_3,textvariable=self.var_severe,font=("times new roman",12,"bold"),state="readonly",width=10)
        threat_combo["values"]=("Select","normal checkup(green)","not well(yellow)","uneasy(yellow)","severe(red)")
        threat_combo.current(0)
        threat_combo.grid(row=0,column=4,padx=3,pady=10)

        sosbtn1=Button(frame_3,text="EMERGENCY",command=self.add_emergencybutton,width=11,font=("times new roman",16,"bold"),bg="red",fg="white",activebackground="red",activeforeground="white")
        sosbtn1.grid(row=0,column=5,padx=10)

        title=Label(right_frame,text="*Carefully select resgistration number",font=("times new roman",15,"bold"),bg="light blue",fg="green")
        title.place(x=0,y=90,width=565,height=30)
        title=Label(right_frame,text="*In Case of emergency press emergency button with respective room no.",font=("times new roman",12,"bold"),bg="light blue",fg="green")
        title.place(x=0,y=120,width=565,height=30)

    #frame
        frame_4=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Data:",font=("times new roman",12,"bold"))
        frame_4.place(x=0,y=150,width=565,height=350)   
    #data box   
        scroll_x=ttk.Scrollbar(frame_4,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_4,orient=VERTICAL)

        self.patient_records=ttk.Treeview(frame_4,columns=("agegroup","profession","healthproblem","room","patientname","resgistration","bp","gender","weight","height","oxygen","heart","dor","phone","radio1"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.patient_records.xview)
        scroll_y.config(command=self.patient_records.yview)
        
        self.patient_records.heading("agegroup",text="Age Group")
        self.patient_records.heading("profession",text="Profession")
        self.patient_records.heading("healthproblem",text="Health Issue")
        self.patient_records.heading("room",text="Room Number")
        self.patient_records.heading("patientname",text="Patient Name")
        self.patient_records.heading("resgistration",text="Registration Number")
        self.patient_records.heading("bp",text="Blood Pressure")
        self.patient_records.heading("gender",text="Gender")
        self.patient_records.heading("weight",text="Weight")
        self.patient_records.heading("height",text="Height")
        self.patient_records.heading("oxygen",text="Oxygen Rate")
        self.patient_records.heading("heart",text="Heart Rate")
        self.patient_records.heading("dor",text="Registration Date")
        self.patient_records.heading("phone",text="Phone")
        self.patient_records.heading("radio1",text="Photo")
        self.patient_records["show"]="headings"

        self.patient_records.column("agegroup",width=100)
        self.patient_records.column("profession",width=100)
        self.patient_records.column("healthproblem",width=100)
        self.patient_records.column("room",width=100)
        self.patient_records.column("patientname",width=100)
        self.patient_records.column("resgistration",width=140)
        self.patient_records.column("bp",width=100)
        self.patient_records.column("gender",width=100)
        self.patient_records.column("weight",width=100)
        self.patient_records.column("height",width=100)
        self.patient_records.column("oxygen",width=100)
        self.patient_records.column("heart",width=100)
        self.patient_records.column("dor",width=100)
        self.patient_records.column("phone",width=100)
        self.patient_records.column("radio1",width=100)

        self.patient_records.pack(fill=BOTH,expand=1)
        self.patient_records.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_agegroup.get()=="Select Age Group" or self.var_patientname.get()=="" or self.var_registration.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into patient_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.var_agegroup.get(),
                                                                                                         self.var_profession.get(),
                                                                                                         self.var_healthproblem.get(),
                                                                                                         self.var_room.get(),
                                                                                                         self.var_patientname.get(),
                                                                                                         self.var_registration.get(),
                                                                                                         self.var_bp.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_weight.get(),
                                                                                                         self.var_height.get(),
                                                                                                         self.var_oxygen.get(),
                                                                                                         self.var_heart.get(),
                                                                                                         self.var_dor.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_radio1.get()

                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Patient Data Added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                
    #===================fetch data========================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from patient_data")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.patient_records.delete(*self.patient_records.get_children())
            for i in data:
                self.patient_records.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==================update data========================= 
    def get_cursor(self,event=""):
        cursor_focus=self.patient_records.focus()
        content=self.patient_records.item(cursor_focus)
        data=content["values"]

        self.var_agegroup.set(data[0]),
        self.var_profession.set(data[1]),
        self.var_healthproblem.set(data[2]),
        self.var_room.set(data[3]),
        self.var_patientname.set(data[4]),
        self.var_registration.set(data[5]),
        self.var_bp.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_weight.set(data[8]),
        self.var_height.set(data[9]),
        self.var_oxygen.set(data[10]),
        self.var_heart.set(data[11]),
        self.var_dor.set(data[12]),
        self.var_phone.set(data[13]),
        self.var_radio1.set(data[14])

    #=========update function=====================
    def update_data(self):
        if self.var_agegroup.get()=="Select Age Group" or self.var_patientname.get()=="" or self.var_registration.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Updatedata=messagebox.askyesno("Updatedata","Do you want to update this patient info",parent=self.root)
                if Updatedata>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update patient_data set agegroup=%s,profession=%s,healthproblem=%s,room=%s,patientname=%s,bp=%s,gender=%s,weight=%s,height=%s,oxygen=%s,heart=%s,dor=%s,phone=%s,photo=%s where registration=%s",(

                                                                                                                                                                                                                    self.var_agegroup.get(),
                                                                                                                                                                                                                    self.var_profession.get(),
                                                                                                                                                                                                                    self.var_healthproblem.get(),
                                                                                                                                                                                                                    self.var_room.get(),
                                                                                                                                                                                                                    self.var_patientname.get(),
                                                                                                                                                                                                                    self.var_bp.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_weight.get(),
                                                                                                                                                                                                                    self.var_height.get(),
                                                                                                                                                                                                                    self.var_oxygen.get(),
                                                                                                                                                                                                                    self.var_heart.get(),
                                                                                                                                                                                                                    self.var_dor.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_registration.get()
                                                                                                                                                                                                                ))
                else:
                    if not Updatedata:
                        return
                messagebox.showinfo("Success","Patient details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #============delete function=================
    def delete_data(self):
        if self.var_registration.get()=="":
            messagebox.showerror("Error","Patient registration number is required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Patient Data Delete","Are you the certified operator to use this function",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                    my_cursor=conn.cursor()
                    sql="delete from patient_data where registration=%s"
                    val=(self.var_registration.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted patient",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #====================reset function=================
    def reset_data(self):
        self.var_agegroup.set("Select Age Group")
        self.var_profession.set("Select Profession")
        self.var_healthproblem.set("Select Health Issue")
        self.var_room.set("Select Room")
        self.var_patientname.set("")
        self.var_registration.set("")
        self.var_bp.set("")
        self.var_gender.set("")
        self.var_weight.set("")
        self.var_height.set("")
        self.var_oxygen.set("")
        self.var_heart.set("")
        self.var_dor.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    #==================dataset for images===========================
    def generate_dataset(self):
        if self.var_agegroup.get()=="Select Age Group" or self.var_patientname.get()=="" or self.var_registration.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from patient_data")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update patient_data set agegroup=%s,profession=%s,healthproblem=%s,room=%s,patientname=%s,bp=%s,gender=%s,weight=%s,height=%s,oxygen=%s,heart=%s,dor=%s,phone=%s,photo=%s where registration=%s",(

                                                                                                                                                                                                                    self.var_agegroup.get(),
                                                                                                                                                                                                                    self.var_profession.get(),
                                                                                                                                                                                                                    self.var_healthproblem.get(),
                                                                                                                                                                                                                    self.var_room.get(),
                                                                                                                                                                                                                    self.var_patientname.get(),
                                                                                                                                                                                                                    self.var_bp.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_weight.get(),
                                                                                                                                                                                                                    self.var_height.get(),
                                                                                                                                                                                                                    self.var_oxygen.get(),
                                                                                                                                                                                                                    self.var_heart.get(),
                                                                                                                                                                                                                    self.var_dor.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_registration.get()==id+1
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
                        file_name_path="datapatient/patientname."+str(id)+"."+str(img_id)+".jpg"
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

    def add_emergencybutton(self):
        if self.var_roomno.get()=="Select Room" or self.var_severe.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into emergencyservice values(%s,%s)",(
                                                                                                         self.var_roomno.get(),
                                                                                                         self.var_severe.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Emergency message sent to staff",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Are you sure you want to exit patient registration tab?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return
    def chatbot(self):
        self.new_window2=Toplevel(self.root)
        self.app=sage(self.new_window2)

if __name__ =="__main__":
    root=Tk()
    obj=Patient(root)
    root.mainloop()
