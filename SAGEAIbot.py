from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 


class sage:
    def __init__(self,root):
        self.root=root
        self.root.title("Sage")
        self.root.geometry("750x630+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open(r'D:\IPProjectFinal\icons\sagelogo.jpg')
        img_chat=img_chat.resize((210,80),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='Sage Personalised AI',font=('hammerhead',30,'bold'),fg='cyan',bg='black')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=800)
        btn_frame.pack()

        label_1=Label(btn_frame,text='Chat With Sage',font=('hammerhead',14,'bold'),fg='cyan',bg='grey')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=33,font=('Arial',17,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('hammerhead',16,'bold'),width=5,bg='green',)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clare=Button(btn_frame,text="Clear Memory",command=self.clear,font=('hammerhead',15,'bold'),width=12,bg='red',fg='white',activebackground="red",activeforeground="white")
        self.clare.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('hammerhead',14,'bold'),fg='cyan',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

#===================defining function====================
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normalcheckup')

        elif(self.entry.get()=='sup'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normal checkup')

        elif(self.entry.get()=='yo'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normal checkup')

        elif(self.entry.get()=='hey there'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normal checkup')

        elif(self.entry.get()=='hey'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normal checkup')

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user! (•◡•) / for check up please use normal checkup')

        elif(self.entry.get()=='sage'):
            self.text.insert(END,'\n\n'+'Sage: Hello there user!(✿◠‿◠)  for check up please use normal checkup')

        elif(self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Sage: I am fine Thanks for asking about me, How are u User?')
        
        elif(self.entry.get()=='hwru'):
            self.text.insert(END,'\n\n'+'Sage: I am fine Thanks for asking about me, How are u User?')

        elif(self.entry.get()=='how are you doing'):
            self.text.insert(END,'\n\n'+'Sage: I am fine Thanks for asking about me, How are u User?')
        
        elif(self.entry.get()=='how do yo do'):
            self.text.insert(END,'\n\n'+'Sage: I am fine Thanks for asking about me, How are u User?')

        elif(self.entry.get()=='great'):
            self.text.insert(END,'\n\n'+'Sage: Its great to hear that from u User!')

        elif(self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Sage: Its great to hear that from u User!')

        elif(self.entry.get()=='awesome'):
            self.text.insert(END,'\n\n'+'Sage: Its great to hear that from u User!')
        
        elif(self.entry.get()=='fine'):
            self.text.insert(END,'\n\n'+'Sage: Its great to hear that from u User!')
        
        elif(self.entry.get()=='good'):
            self.text.insert(END,'\n\n'+'Sage: Its great to hear that from u User!')

        elif(self.entry.get()=='who is your creator'):
            self.text.insert(END,'\n\n'+'Sage: My Creator is Sansprime a.k.a Shubhayu')

        elif(self.entry.get()=='who created you'):
            self.text.insert(END,'\n\n'+'Sage: My Creator is Sansprime a.k.a Shubhayu')

        elif(self.entry.get()=='who made you'):
            self.text.insert(END,'\n\n'+'Sage: My Creator is Sansprime a.k.a Shubhayu')

        elif(self.entry.get()=='who developed you'):
            self.text.insert(END,'\n\n'+'Sage: My Creator is Sansprime a.k.a Shubhayu')
        
        elif(self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Sage: My name is Sage! nice to meet you (✿◠‿◠)')

        elif(self.entry.get()=='version'):
            self.text.insert(END,'\n\n'+'Sage: My current build is at beta test 3.8')

        elif(self.entry.get()=='Version'):
            self.text.insert(END,'\n\n'+'Sage: My current build is at beta test 3.8')

        elif(self.entry.get()=='build'):
            self.text.insert(END,'\n\n'+'Sage: My current build is at beta test 3.8')

        elif(self.entry.get()=='what is your version'):
            self.text.insert(END,'\n\n'+'Sage: My current build is at beta test 3.8')

        elif(self.entry.get()=='Normal Checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,symptoms-')

        elif(self.entry.get()=='normal checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,symptoms-')

        elif(self.entry.get()=='Normal checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,symptoms-')

        elif(self.entry.get()=='normal Checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,symptoms-')

        elif(self.entry.get()=='Checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,symptoms-')

        elif(self.entry.get()=='checkup'):
            self.text.insert(END,'\n\n'+'Sage: Welcome user to ai self reponse chatbot nurse! kindly use key word-temp,temperature,bp,bloodpressure,heartrate,oxygenrate,oxyrate,symptoms-')

        elif(self.entry.get()=='temp'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your temperature in fahrenheit format -number F-:')

        elif(self.entry.get()=='97 F'):
            self.text.insert(END,'\n\n'+'Sage: Normal Tempreature!')

        elif(self.entry.get()=='98 F'):
            self.text.insert(END,'\n\n'+'Sage: Normal Tempreature!')

        elif(self.entry.get()=='99 F'):
            self.text.insert(END,'\n\n'+'Sage: Normal Tempreature!')

        elif(self.entry.get()=='100 F'):
            self.text.insert(END,'\n\n'+'Sage: High Temperature fever requires attention!')

        elif(self.entry.get()=='101 F'):
            self.text.insert(END,'\n\n'+'Sage: High Temperature fever requires attention!')

        elif(self.entry.get()=='102 F'):
            self.text.insert(END,'\n\n'+'Sage: High Temperature fever requires attention!')

        elif(self.entry.get()=='80 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: Low BP!')

        elif(self.entry.get()=='90 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: Normal BP!')

        elif(self.entry.get()=='100 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: Normal BP!')

        elif(self.entry.get()=='120 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: Normal BP!')

        elif(self.entry.get()=='130 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: High BP requires attention!')

        elif(self.entry.get()=='140 mmHg'):
            self.text.insert(END,'\n\n'+'Sage: High BP requires attention!')

        elif(self.entry.get()=='temp'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your temperature in fahrenheit format -number F-:')

        elif(self.entry.get()=='temperature'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your temperature in fahrenheit format -number F-:')

        elif(self.entry.get()=='bp'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your Blood Pressure in millimeter of mercury format -number mmHg-:')

        elif(self.entry.get()=='bloodpressure'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your Blood Pressure in millimeter of mercury format -number mmHg-:')
        
        elif(self.entry.get()=='heartrate'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your heartrate in beats per minute format -number bpm-:')

        elif(self.entry.get()=='oxygenrate'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your oxygen sturation level in format -number %-:')

        elif(self.entry.get()=='oxyrate'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your oxygen sturation level in format -number %-:')

        elif(self.entry.get()=='symptoms'):
            self.text.insert(END,'\n\n'+'Sage: User kindly enter your symptoms - fever, cold/cough, vomit, diarrhea, nausea, etc.')
            
        elif(self.entry.get()=='what is is your purpose'):
            self.text.insert(END,'\n\n'+'Sage: my main purpose is as an mediacal assistant for doctors but currently speaking i am in chatbot state')

        elif(self.entry.get()=='in what language are you created in'):
            self.text.insert(END,'\n\n'+'Sage: Python!')

        elif(self.entry.get()=='what modules do you use'):
            self.text.insert(END,'\n\n'+'Sage: for all this graphical interface i am using Tkinter,Matplotlib,pandas,numpy,csv,face_recognition,legacy_core and other modules as well.')

        elif(self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Sage: Bye! user thanks for chatting with me (✿◠‿◠) ')

        elif(self.entry.get()=='What is AI'):
            self.text.insert(END,'\n\n'+'Sage: Artificial intelligence (AI) is the ability of a computer or a robot controlled by a computer to do tasks that are usually done by humans because they require human intelligence and discernment.')

        elif(self.entry.get()=='What is chatbot'):
            self.text.insert(END,'\n\n'+'Sage: a computer program designed to simulate conversation with human users, even i am a chatbot!')

        elif(self.entry.get()=='Use of ai in medical stream'):
            self.text.insert(END,'\n\n'+'Sage: Artificially intelligent computer systems are used extensively in medical sciences. Common applications include diagnosing patients, end-to-end drug discovery and development, improving communication between physician and patient, transcribing medical documents, such as prescriptions, and remotely treating patients.')

        else:
            self.text.insert(END,"\n\n"+"Bot: function not understood Please type again! ⊙_⊙ ")



if __name__ =='__main__':
    root=Tk()
    obj=sage(root)
    root.mainloop()