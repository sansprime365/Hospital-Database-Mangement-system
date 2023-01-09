from tkinter import*
from PIL import Image,ImageTk
from logininpatient import LoginPatient
from logininstaff import LoginStaff
import tkinter
from SAGEAIbot import sage

class LoginMain:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x730+0+0")
        self.root.title("MEDICAL MANAGEMENT SYSTEM")
        #self.root.wm_iconbitmap("medicaldatabase.ico")

        imglgn=Image.open(r"D:\IPProjectFinal\backgrounds\26358.png")
        imglgn=imglgn.resize((1290,730),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(imglgn)

        lgnbgimg=Label(self.root,image=self.photoimg)
        lgnbgimg.place(x=0,y=0,width=1290,height=730)

        main_framestaff=Frame(lgnbgimg,bd=2,bg="powder blue")
        main_framestaff.place(x=180,y=220,width=350,height=300)

        main_framepatient=Frame(lgnbgimg,bd=2,bg="powder blue")
        main_framepatient.place(x=760,y=220,width=350,height=300)

        title=Label(self.root,text="MEDICAL MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="powder blue",fg="orange")
        title.place(x=220,y=80,width=810,height=60)

        title=Label(self.root,text="Welcome User to Home Tab",font=("times new roman",35,"bold"),bg="powder blue",fg="orange")
        title.place(x=220,y=150,width=810,height=60)

        title=Label(self.root,text="Login as Patient",font=("times new roman",12,"bold"),bg="black",fg="white")
        title.place(x=270,y=400,width=150,height=25)

        title=Label(self.root,text="Login as Staff",font=("times new roman",12,"bold"),bg="black",fg="white")
        title.place(x=850,y=400,width=150,height=25)

        #=========buttons=============
        patientbtn1=Button(self.root,bg="white",command=self.patient_login,text="Patient Login/Register",font=("times new roman",15,"bold"),fg="black",activebackground="white",foreground="black",borderwidth=0)
        patientbtn1.place(x=210,y=440,width=290,height=55)

        staffbtn1=Button(self.root,bg="white",command=self.staff_login,text="Staff Login/Register",font=("times new roman",15,"bold"),fg="black",activebackground="white",foreground="black",borderwidth=0)
        staffbtn1.place(x=790,y=440,width=290,height=55)

        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\exitbttn.png")
        imgbttn1=imgbttn1.resize((50,50),Image.ANTIALIAS)
        self.photoimgexit=ImageTk.PhotoImage(imgbttn1)

        imgbttn1=Image.open(r"D:\IPProjectFinal\icons\chatbotbttn.png")
        imgbttn1=imgbttn1.resize((50,50),Image.ANTIALIAS)
        self.photoimgchat=ImageTk.PhotoImage(imgbttn1)

        exitbttn = Button(self.root,image=self.photoimgexit,command=self.Exit,cursor="hand2",bg="white",width=50,height=60,activebackground="white")
        exitbttn.place(x=1180, y=610)

        exitbttn = Button(self.root,image=self.photoimgchat,command=self.chatbot,cursor="hand2",bg="white",width=50,height=60,activebackground="white")
        exitbttn.place(x=1120, y=610)

        imglb=Image.open(r"D:\IPProjectFinal\icons\pngwin1.png")
        imglb=imglb.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(imglb)

        lframe=Label(self.root,image=self.photoimg1,background="powder blue")
        lframe.place(x=880,y=250,width=100,height=100)

        imglb=Image.open(r"D:\IPProjectFinal\icons\pngwing11.com.png")
        imglb=imglb.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(imglb)

        lframe=Label(self.root,image=self.photoimg2,background="powder blue")
        lframe.place(x=300,y=250,width=100,height=100)


        #=========def login tabs========
    def patient_login(self):
        self.new_window1=Toplevel(self.root)
        self.app=LoginPatient(self.new_window1)
    
    def staff_login(self):
        self.new_window2=Toplevel(self.root)
        self.app=LoginStaff(self.new_window2)

    def chatbot(self):
        self.new_window3=Toplevel(self.root)
        self.app=sage(self.new_window3)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Are you sure you want to exit this tab?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return


if __name__ =="__main__":
    root=Tk()
    obj=LoginMain(root)
    root.mainloop()