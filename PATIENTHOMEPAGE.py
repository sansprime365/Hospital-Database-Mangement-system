from tkinter import*
import tkinter
from PIL import Image,ImageTk
import os
from patientregistry import Patient
from SAGEAIbot import sage
from train1 import Train
from aifacerecognition1 import FaceRecognition
from patientattendancereport import Patientattendance


class Patientmainpage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x735+0+0")
        self.root.title("Main Window")
        
        imgbg=Image.open(r"D:\IPProjectFinal\backgrounds\19272.jpg")
        imgbg=imgbg.resize((1300,735),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(imgbg)

        f_1bg=Label(self.root,image=self.photoimg13)
        f_1bg.place(x=0,y=0,width=1300,height=735)

        titlemain=Label(f_1bg,text="Patient Database System",font=("times new roman",35,"bold"),bg="light gray",fg="orange")
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
        b1bttn = Button(f_1bg,image=self.photoimgbt2,command=self.Patientr,cursor="hand2",bg="white",width=208,height=110)
        b1bttn.place(x=50, y=200)
        b1chat = Button(f_1bg,text="Patient Register",command=self.Patientr, font=("Arial", 15,"bold"),cursor="hand2",width=17)
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

        b5bttn = Button(f_1bg,image=self.photoimgbt5,command=self.patient_attendance,cursor="hand2",bg="white",width=208,height=110)
        b5bttn.place(x=50, y=540)
        b5chat = Button(f_1bg,text="Patient Attendance",command=self.patient_attendance, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b5chat.place(x=50, y=650)

        b6bttn = Button(f_1bg,image=self.photoimgbt6,command=self.open_img,cursor="hand2",bg="white",width=208,height=110)
        b6bttn.place(x=310, y=540)
        b6chat = Button(f_1bg,text="Patient Profile Data",command=self.open_img, font=("Arial", 15,"bold"),cursor="hand2",width=17)
        b6chat.place(x=310, y=650)

        main2_frame=Frame(f_1bg,bd=2,bg="powder blue")
        main2_frame.place(x=680,y=190,width=550,height=500)

        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\exitbttn.png")
        imgbttn1=imgbttn1.resize((50,50),Image.ANTIALIAS)
        self.photoimgexit=ImageTk.PhotoImage(imgbttn1)
        exitbttn = Button(self.root,image=self.photoimgexit,command=self.Exit,cursor="hand2",bg="white",width=0,height=60,activebackground="white")
        exitbttn.place(x=1140, y=20)

        titlemain=Label(main2_frame,text="Welcome to patient database system",font=("times new roman",20,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=0,width=550,height=30)
        titlemain=Label(main2_frame,text="------------------------------------------------------------",font=("times new roman",20,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=30,width=550,height=30)
        titlemain=Label(main2_frame,text="1)If you are new to system please click patient on register.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=80,width=545,height=30)
        titlemain=Label(main2_frame,text="2)Add your details and don't forget to register your images.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=110,width=550,height=30)
        titlemain=Label(main2_frame,text="3)After adding your details click on train data.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=140,width=440,height=30)
        titlemain=Label(main2_frame,text="4)Then click on Cam Recognition to capture your presence.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=170,width=550,height=30)
        titlemain=Label(main2_frame,text="5)Then click on patient attendance and import",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=200,width=440,height=30)
        titlemain=Label(main2_frame,text="attendancepatient.csv.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=230,width=280,height=30)
        titlemain=Label(main2_frame,text="6)Then click on patient profile to check you captured images.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=260,width=560,height=30)
        titlemain=Label(main2_frame,text="7)To report emergency click on register patient and select",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=290,width=535,height=30)
        titlemain=Label(main2_frame,text="room number and severity of emergency.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=320,width=430,height=30)
        titlemain=Label(main2_frame,text="8)To consult click on the chatbot to consult yourself.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=350,width=490,height=30)
        titlemain=Label(main2_frame,text="9)To exit click on the exit button on topright corner.",font=("times new roman",15,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=380,width=490,height=30)
        titlemain=Label(main2_frame,text="Thankyou For Using Sage Management System",font=("times new roman",19,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=450,width=550,height=30)
        titlemain=Label(main2_frame,text="------------------------------------------------------------",font=("times new roman",20,"bold"),bg="powder blue",fg="black")
        titlemain.place(x=0,y=420,width=550,height=30)

    #==============define buttons==============
    def chatbot(self):
        self.new_window2=Toplevel(self.root)
        self.app=sage(self.new_window2)

    def Patientr(self):
        self.new_window3=Toplevel(self.root)
        self.app=Patient(self.new_window3)

    def open_img(self):
        os.startfile("datapatient")

    def train_data(self):
        self.new_window4=Toplevel(self.root)
        self.app=Train(self.new_window4)

    def face_recognition(self):
        self.new_window5=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window5)

    def patient_attendance(self):
        self.new_window6=Toplevel(self.root)
        self.app=Patientattendance(self.new_window6)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Are you sure you wanna exit this tab?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return

if __name__ =="__main__":
    root=Tk()
    obj=Patientmainpage(root)
    root.mainloop()