from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import mysql.connector
import os
from staffregistry import Staff
from SAGEAIbot import sage
from train2 import Train
from aifacerecognition2 import FaceRecognition
from staffattendancereport import Staffattendance


class Staffmainpage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x735+0+0")
        self.root.title("Main Window")
        
        imgbg=Image.open(r"D:\IPProjectFinal\backgrounds\19272.jpg")
        imgbg=imgbg.resize((1300,735),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(imgbg)

        f_1bg=Label(self.root,image=self.photoimg13)
        f_1bg.place(x=0,y=0,width=1300,height=735)

        titlemain=Label(f_1bg,text="Staff Database System",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
        titlemain.place(x=0,y=20,width=1287,height=60)

        #============buttons==================
        #============images===================
        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\2002.i039.010_chatbot_messenger_ai_isometric_set-05.jpg")
        imgbttn1=imgbttn1.resize((170,150),Image.ANTIALIAS)
        self.photoimgbt1=ImageTk.PhotoImage(imgbttn1)
        
        imgbttn2=Image.open(r"D:\IPProjectFinal\icons\5879.jpg")
        imgbttn2=imgbttn2.resize((170,150),Image.ANTIALIAS)
        self.photoimgbt2=ImageTk.PhotoImage(imgbttn2)

        imgbttn3=Image.open(r"D:\IPProjectFinal\icons\pngwing9.com.png")
        imgbttn3=imgbttn3.resize((110,90),Image.ANTIALIAS)
        self.photoimgbt3=ImageTk.PhotoImage(imgbttn3)

        imgbttn4=Image.open(r"D:\IPProjectFinal\icons\pngwing4.com.png")
        imgbttn4=imgbttn4.resize((150,130),Image.ANTIALIAS)
        self.photoimgbt4=ImageTk.PhotoImage(imgbttn4)

        imgbttn5=Image.open(r"D:\IPProjectFinal\icons\5847.jpg")
        imgbttn5=imgbttn5.resize((170,150),Image.ANTIALIAS)
        self.photoimgbt5=ImageTk.PhotoImage(imgbttn5)

        imgbttn6=Image.open(r"D:\IPProjectFinal\icons\pngwing7.com.png")
        imgbttn6=imgbttn6.resize((110,100),Image.ANTIALIAS)
        self.photoimgbt6=ImageTk.PhotoImage(imgbttn6)
        #==============switch buttons==============
        b1bttn = Button(f_1bg,image=self.photoimgbt2,command=self.Staffr,cursor="hand2",bg="white",width=208,height=110)
        b1bttn.place(x=50, y=200)
        b1chat = Button(f_1bg,text="Staff Registry",command=self.Staffr, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b1chat.place(x=50, y=310)

        b2bttn = Button(f_1bg,image=self.photoimgbt1,command=self.chatbot,cursor="hand2",bg="white",width=208,height=110)
        b2bttn.place(x=310, y=200)
        b2chat = Button(f_1bg,text="Sage AI Chatbot",command=self.chatbot, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b2chat.place(x=310, y=310)

        b3bttn = Button(f_1bg,image=self.photoimgbt3,command=self.train_data,cursor="hand2",bg="white",width=208,height=110)
        b3bttn.place(x=50, y=370)
        b3chat = Button(f_1bg,text="Train Data",command=self.train_data, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b3chat.place(x=50, y=480)

        b4bttn = Button(f_1bg,image=self.photoimgbt4,command=self.face_recognition,cursor="hand2",bg="white",width=208,height=110)
        b4bttn.place(x=310, y=370)
        b4chat = Button(f_1bg,text="Cam Recognition",command=self.face_recognition, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b4chat.place(x=310, y=480)

        b5bttn = Button(f_1bg,image=self.photoimgbt5,command=self.staff_attendance,cursor="hand2",bg="white",width=208,height=110)
        b5bttn.place(x=50, y=540)
        b5chat = Button(f_1bg,text="Staff Attendance",command=self.staff_attendance, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b5chat.place(x=50, y=650)

        b6bttn = Button(f_1bg,image=self.photoimgbt6,command=self.open_img,cursor="hand2",bg="white",width=208,height=110)
        b6bttn.place(x=310, y=540)
        b6chat = Button(f_1bg,text="Staff Profile Data",command=self.open_img, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b6chat.place(x=310, y=650)

        main2_frame=Frame(f_1bg,bd=2,bg="powder blue")
        main2_frame.place(x=680,y=170,width=550,height=530)

        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\exitbttn.png")
        imgbttn1=imgbttn1.resize((50,50),Image.ANTIALIAS)
        self.photoimgexit=ImageTk.PhotoImage(imgbttn1)
        exitbttn = Button(self.root,image=self.photoimgexit,command=self.Exit,cursor="hand2",bg="white",width=0,height=60,activebackground="white")
        exitbttn.place(x=1140, y=20)

    #frame
        frame_4=LabelFrame(main2_frame,bd=2,relief=RIDGE,text="Registered Patients Data:",font=("times new roman",12,"bold"))
        frame_4.place(x=0,y=0,width=545,height=400)   
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
        self.fetch_data()

        #=========emergency================
        frame_5=LabelFrame(main2_frame,bd=2,relief=RIDGE,text="Emergency Issues:",font=("times new roman",12,"bold"))
        frame_5.place(x=0,y=400,width=545,height=120)

        scroll_x=ttk.Scrollbar(frame_5,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_5,orient=VERTICAL)

        self.emergency_records=ttk.Treeview(frame_5,columns=("RoomNumber","Severity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.emergency_records.xview)
        scroll_y.config(command=self.emergency_records.yview)
        
        self.emergency_records.heading("RoomNumber",text="RoomNumber")
        self.emergency_records.heading("Severity",text="Severity")
        self.emergency_records["show"]="headings"

        self.emergency_records.column("RoomNumber",width=100)
        self.emergency_records.column("Severity",width=100)
        
        self.emergency_records.pack(fill=BOTH,expand=1)
        self.fetch_data1()

    def fetch_data1(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from emergencyservice")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.emergency_records.delete(*self.emergency_records.get_children())
            for i in data:
                self.emergency_records.insert("",END,values=i)
            conn.commit()
        conn.close()


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

    #==============define buttons==============
    def chatbot(self):
        self.new_window2=Toplevel(self.root)
        self.app=sage(self.new_window2)

    def Staffr(self):
        self.new_window3=Toplevel(self.root)
        self.app=Staff(self.new_window3)

    def open_img(self):
        os.startfile("datastaff")

    def train_data(self):
        self.new_window4=Toplevel(self.root)
        self.app=Train(self.new_window4)

    def face_recognition(self):
        self.new_window5=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window5)

    def staff_attendance(self):
        self.new_window6=Toplevel(self.root)
        self.app=Staffattendance(self.new_window6)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Are you sure you wanna exit this tab?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return

if __name__ =="__main__":
    root=Tk()
    obj=Staffmainpage(root)
    root.mainloop()