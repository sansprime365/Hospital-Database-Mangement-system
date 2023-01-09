from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from PATIENTHOMEPAGE import Patientmainpage
import tkinter

def main():
    win=Tk()
    app=LoginPatient(win)
    win.mainloop()

class LoginPatient:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+0+0")
        self.root.title("Patient Login")

        main_frame=Frame(self.root,bd=2,bg="powder blue")
        main_frame.place(x=0,y=0,width=900,height=600)

        main_frame=Frame(main_frame,bd=2,bg="black")
        main_frame.place(x=200,y=130,width=500,height=370)

        imglb=Image.open(r"D:\IPProjectFinal\icons\pngwing11.com.png")
        imglb=imglb.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(imglb)

        lframe=Label(self.root,image=self.photoimg1,background="powder blue")
        lframe.place(x=400,y=30,width=100,height=100)

        label=Label(main_frame,text="Patient Login",font=("times new roman",30,"bold"),bg="black",fg="white")
        label.place(x=120,y=0,width=270,height=60)

        label=Label(main_frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        label.place(x=100,y=70)

        label=Label(main_frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        label.place(x=100,y=150)

        self.txtuser=Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=100,y=110,width=230)

        self.txtpass=Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=100,y=190,width=230)

        loginbtn1=Button(main_frame,text="Login",command=self.login,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="powder blue")
        loginbtn1.place(y=240,x=150)

        registerbtn1=Button(main_frame,command=self.rgster_window,text="Register Account",width=11,font=("times new roman",12,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",borderwidth=0)
        registerbtn1.place(y=290,x=20,width=150)

        forgotpasbtn1=Button(main_frame,text="Forgot Password",command=self.forgot_passwordid,width=11,font=("times new roman",12,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white",borderwidth=0)
        forgotpasbtn1.place(y=320,x=20,width=150)

    def rgster_window(self):
        self.new_window=Toplevel(self.root)
        self.app=patientloginID(self.new_window)

    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror('Error Occured',"All fields are reqired!")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="sage15ai":
            messagebox.showinfo("Login Success","Welcome to Patient Database!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from patientuserid where username=%s and Confirmpass=%s",(
                                                                                                self.txtuser.get(),
                                                                                                self.txtpass.get() 
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_menu=messagebox.askyesno("YesNo","Access only to respective patients")
                if open_menu>0:
                    self.new_tab=Toplevel(self.root)
                    self.app=Patientmainpage(self.new_tab)
                else:
                    if not open_menu:
                        return
            conn.commit()
            conn.close()
#=======================resetpassword========================
    def reset_pass(self):
        if self.security_combo.get()=="Select Question":
            messagebox.showerror("Error","Select the security question")
        elif self.securitypa.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.newpass1.get()=="":
            messagebox.showerror("Error","Please enter your new password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
            my_cursor=conn.cursor()
            qury=("select * from patientuserid where username=%s and securityq=%s and securityans=%s")
            vlaue=(self.txtuser.get(),self.security_combo.get(),self.securitypa.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer")
            else:
                query=("update patientuserid set Confirmpass=%s where username=%s")
                value=(self.newpass1.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset successfully, please login")
#====================forgotpassword=======================
    def forgot_passwordid(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please write the respective username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
            my_cursor=conn.cursor()
            query=("select * from patientuserid where username=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("User Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="black",fg="white")
                l.place(x=0,y=10,relwidth=1)

                security1=Label(self.root2,text="Security Question:",font=("times new roman",15,"bold"),bg="black",fg="white")
                security1.place(x=50,y=80)
                self.security_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly",width=20)
                self.security_combo["values"]=("Select Question","bestie's name","nickname","pet's name","school name","favorite song","favourite colour")
                self.security_combo.current(0)
                self.security_combo.place(x=50,y=110)

                security2=Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),bg="black",fg="white")
                security2.place(x=50,y=150)
                self.securitypa=ttk.Entry(self.root2,font=("times new roman",15,"bold"),width=20)
                self.securitypa.place(x=50,y=180)

                newpass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="black",fg="white")
                newpass.place(x=50,y=220)
                self.newpass1=ttk.Entry(self.root2,font=("times new roman",15,"bold"),width=20)
                self.newpass1.place(x=50,y=250)

                loginbtn1=Button(self.root2,text="Reset Password",command=self.reset_pass,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="powder blue")
                loginbtn1.place(y=310,x=90)



class patientloginID:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+0+0")
        self.root.title("Patient ID")

        self.var_username=StringVar()
        self.var_securityq=StringVar()
        self.var_securityans=StringVar()
        self.var_Setpass=StringVar()
        self.var_Confirmpass=StringVar()

        main_frame=Frame(self.root,bd=2,bg="powder blue")
        main_frame.place(x=0,y=0,width=900,height=600)

        main_frame=Frame(main_frame,bd=2,bg="black")
        main_frame.place(x=45,y=110,width=800,height=370)

        label=Label(main_frame,text="Patient UserID Registration",font=("times new roman",30,"bold"),bg="black",fg="white")
        label.place(x=160,y=0,width=480,height=60)

        name1=Label(main_frame,text="Patient User Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        name1.place(x=60,y=60,width=200,height=60)
        name=ttk.Entry(main_frame,textvariable=self.var_username,font=("times new roman",15,"bold"),width=20)
        name.place(x=80,y=100)

        security1=Label(main_frame,text="Security Question:",font=("times new roman",15,"bold"),bg="black",fg="white")
        security1.place(x=60,y=140,width=200,height=60)
        security_combo=ttk.Combobox(main_frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly",width=20)
        security_combo["values"]=("Select Question","bestie's name","nickname","pet's name","school name","favorite song","favourite colour")
        security_combo.current(0)
        security_combo.place(x=80,y=180)

        security2=Label(main_frame,text="Security Answer:",font=("times new roman",15,"bold"),bg="black",fg="white")
        security2.place(x=405,y=140,width=200,height=60)
        securitypa=ttk.Entry(main_frame,textvariable=self.var_securityans,font=("times new roman",15,"bold"),width=20)
        securitypa.place(x=430,y=180)

        pass1=Label(main_frame,text="Set Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pass1.place(x=70,y=210,width=140,height=60)
        passwrd=ttk.Entry(main_frame,textvariable=self.var_Setpass,font=("times new roman",15,"bold"),width=20)
        passwrd.place(x=80,y=250)

        pass1=Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pass1.place(x=405,y=210,width=200,height=60)
        passwrd=ttk.Entry(main_frame,textvariable=self.var_Confirmpass,font=("times new roman",15,"bold"),width=20)
        passwrd.place(x=430,y=250)

        rgstrbtn1=Button(main_frame,text="Register",command=self.registerdata,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="white",borderwidth=0)
        rgstrbtn1.place(y=320,x=480)

        loginbtn1=Button(main_frame,text="Login",command=self.LoginBackButton,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="white",borderwidth=0)
        loginbtn1.place(y=320,x=620)

    def registerdata(self):
        if self.var_username.get()=="" or self.var_securityq.get()=="" or self.var_securityans.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_Setpass.get()!=self.var_Confirmpass.get():
            messagebox.showerror("Error","Password must be same!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
            my_cursor=conn.cursor()
            query=("select * from patientuserid where username=%s")
            value=(self.var_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","UserID already exists use another one")
            else:
                my_cursor.execute("insert into patientuserid values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_username.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securityans.get(),
                                                                                        self.var_Setpass.get(),
                                                                                        self.var_Confirmpass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered patient data")
    def LoginBackButton(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Do you want to return to login page?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return

if __name__ =="__main__":
    main()