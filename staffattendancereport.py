from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata=[]
class Staffattendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1310x730+0+0")
        self.root.title("Staff Attendance Report")

        #=========variables===============
        self.var_RegistrationNo=StringVar()
        self.var_StaffName=StringVar()
        self.var_Dept=StringVar()
        self.var_Age=StringVar()
        self.var_Time=StringVar()
        self.var_Date=StringVar()
        self.var_Attendance=StringVar()

        imgpr1=Image.open(r"D:\IPProjectFinal\backgrounds\v870-mynt-06.jpg")
        imgpr1=imgpr1.resize((1310,735),Image.ANTIALIAS)
        self.photoimgprbg1=ImageTk.PhotoImage(imgpr1)

        bgimg1=Label(self.root,image=self.photoimgprbg1)
        bgimg1.place(x=0,y=0,width=1310,height=735)

        title=Label(bgimg1,text="Staff Attendance Report",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        title.place(x=0,y=0,width=1300,height=60)

        patientreport_frame=Frame(bgimg1,bd=2,bg="powder blue")
        patientreport_frame.place(x=50,y=70,width=1180,height=620)
        # left frame
        left_frame=LabelFrame(patientreport_frame,bd=2,relief=RIDGE,text="Staff Directory",font=("times new roman",12,"bold",))
        left_frame.place(x=20,y=10,width=570,height=600)

        imglb=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imglb=imglb.resize((600,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(imglb)

        lframe=Label(self.root,image=self.photoimg1)
        lframe.place(x=110,y=110,width=500,height=70)

        leftin_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Details",font=("times new roman",12,"bold",))
        leftin_frame.place(x=0,y=90,width=560,height=400)

        registration_label=Label(leftin_frame,text="RegistrationNo:",font=("times new roman",12,"bold"),fg="black")
        registration_label.grid(row=0,column=0,padx=5,pady=5)
        
        registration_entry=ttk.Entry(leftin_frame,textvariable=self.var_RegistrationNo,font=("times new roman",12,"bold"),width=18)
        registration_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        staffname_label=Label(leftin_frame,text="StaffName:",font=("times new roman",12,"bold"),fg="black")
        staffname_label.grid(row=1,column=0,padx=5,pady=5)
        
        staffname_entry=ttk.Entry(leftin_frame,textvariable=self.var_StaffName,font=("times new roman",12,"bold"),width=18)
        staffname_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        dept_label=Label(leftin_frame,text="Department:",font=("times new roman",12,"bold"),fg="black")
        dept_label.grid(row=2,column=0,padx=5,pady=5)
        
        dept_entry=ttk.Entry(leftin_frame,textvariable=self.var_Dept,font=("times new roman",12,"bold"),width=18)
        dept_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        age_label=Label(leftin_frame,text="Age:",font=("times new roman",12,"bold"),fg="black")
        age_label.grid(row=3,column=0,padx=5,pady=5)
        
        age_entry=ttk.Entry(leftin_frame,textvariable=self.var_Age,font=("times new roman",12,"bold"),width=18)
        age_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        time_label=Label(leftin_frame,text="Time:",font=("times new roman",12,"bold"),fg="black")
        time_label.grid(row=0,column=3,padx=5,pady=5)
        
        time_entry=ttk.Entry(leftin_frame,textvariable=self.var_Time,font=("times new roman",12,"bold"),width=16)
        time_entry.grid(row=0,column=4,padx=5,pady=5,sticky=W)

        date_label=Label(leftin_frame,text="Date:",font=("times new roman",12,"bold"),fg="black")
        date_label.grid(row=1,column=3,padx=5,pady=5)
        
        date_entry=ttk.Entry(leftin_frame,textvariable=self.var_Date,font=("times new roman",12,"bold"),width=16)
        date_entry.grid(row=1,column=4,padx=5,pady=5,sticky=W)

        attendance_label=Label(leftin_frame,text="Attendance:",font=("times new roman",12,"bold"),fg="black")
        attendance_label.grid(row=4,column=0,padx=5,pady=5)

        attendance_combo=ttk.Combobox(leftin_frame,textvariable=self.var_Attendance,font=("times new roman",12,"bold"),state="readonly",width=16)
        attendance_combo["values"]=("Select attendance","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=4,column=1,padx=5,pady=5)

        btn_frame=LabelFrame(leftin_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        btn_frame.place(x=0,y=340,width=565,height=40)

    # Import
        Importbtn1=Button(btn_frame,text="ImportCsv",command=self.importCsv,width=15,font=("times new roman",16,"bold"),bg="blue",fg="white")
        Importbtn1.grid(row=0,column=0)

    # Export
        Exportbtn1=Button(btn_frame,text="ExportCsv",command=self.exportCsv,width=14,font=("times new roman",16,"bold"),bg="blue",fg="white")
        Exportbtn1.grid(row=0,column=1)

    # update
        #Updatebtn1=Button(btn_frame,text="Update",width=11,font=("times new roman",16,"bold"),bg="blue",fg="white")
        #Updatebtn1.grid(row=0,column=2)

    # reset
        resetbtn1=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",16,"bold"),bg="blue",fg="white")
        resetbtn1.grid(row=0,column=3)

        #right frame
        right_frame=LabelFrame(patientreport_frame,bd=2,relief=RIDGE,text="Daily Reort Details",font=("times new roman",12,"bold",))
        right_frame.place(x=600,y=10,width=570,height=600)

        imglb1=Image.open(r"D:\IPProjectFinal\icons\sagelogo.jpg")
        imglb1=imglb1.resize((600,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(imglb1)

        lframe=Label(self.root,image=self.photoimg2)
        lframe.place(x=690,y=110,width=500,height=70)

        frame_4=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Data:",font=("times new roman",12,"bold"))
        frame_4.place(x=0,y=90,width=565,height=425)   
    #data box   
        scroll_x=ttk.Scrollbar(frame_4,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_4,orient=VERTICAL)

        self.staff_records=ttk.Treeview(frame_4,columns=("RegistrationNo","StaffName","Dept","Age","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_records.xview)
        scroll_y.config(command=self.staff_records.yview)

        self.staff_records.heading("RegistrationNo",text="RegistrationNo")
        self.staff_records.heading("StaffName",text="StaffName")
        self.staff_records.heading("Dept",text="Dept")
        self.staff_records.heading("Age",text="Age")
        self.staff_records.heading("Time",text="Time")
        self.staff_records.heading("Date",text="Date")
        self.staff_records.heading("Attendance",text="Attendance")
        self.staff_records["show"]="headings"

        self.staff_records.column("RegistrationNo",width=100)
        self.staff_records.column("StaffName",width=100)
        self.staff_records.column("Dept",width=100)
        self.staff_records.column("Age",width=100)
        self.staff_records.column("Time",width=100)
        self.staff_records.column("Date",width=140)
        self.staff_records.column("Attendance",width=100)

        self.staff_records.pack(fill=BOTH,expand=1)

        self.staff_records.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.staff_records.delete(*self.staff_records.get_children())
        for i in rows:
            self.staff_records.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to be exported",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to"+os.path.basement(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.staff_records.focus()
        content=self.staff_records.item(cursor_row)
        rows=content['values']
        self.var_RegistrationNo.set(rows[0])
        self.var_StaffName.set(rows[1])
        self.var_Dept.set(rows[2])
        self.var_Age.set(rows[3])
        self.var_Time.set(rows[4])
        self.var_Date.set(rows[5])
        self.var_Attendance.set(rows[6])
        

    def reset_data(self):
        self.var_RegistrationNo.set("")
        self.var_StaffName.set("")
        self.var_Dept.set("")
        self.var_Age.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_Attendance.set("")
        
if __name__ =="__main__":
    root=Tk()
    obj=Staffattendance(root)
    root.mainloop()