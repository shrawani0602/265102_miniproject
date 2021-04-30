from tkinter import *
w=Tk()
w.title("FITNESS CALCULATOR")
w.geometry('750x550')
c=Canvas(w,width=750,height=550,bg='#e3e3e3')
c.pack()




label_name=Label(text='NAME:',font=('Times New Roman',18),fg='black')
label_name.place(x=50,y=50)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=55)

label_age=Label(text='AGE:',font=('Times New Roman',18),fg='black')
label_age.place(x=450,y=50)

entry_age=Entry(w,bg='white',fg='black')
entry_age.place(x=580,y=55)

label_gender=Label(text='GENDER',font=('Times New Roman',18),fg='black')
label_gender.place(x=50,y=110)

def rad():
    print(var)
var = IntVar()
r1 = Radiobutton(w, text="Male",font=('Times New Roman',15),bg='white', variable=var, value=0,command=rad)
r2 = Radiobutton(w, text="Female",font=('Times New Roman',15),bg='white', variable=var, value=1,command=rad)
r1.place(x=300,y=110)
r2.place(x=550,y=110)

label_name=Label(text='WEIGHT:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=140+20+30)

label_name=Label(text='HEIGHT:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=170+20+30)

label_name=Label(text='BP LOW:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=180+20+20+30)

label_name=Label(text='BP HIGH:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=210+20+20+30)

label_name=Label(text='PULSE RATE:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=240+20+20+30)

label_name=Label(text='RBC COUNT:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=270+20+20+30)

label_name=Label(text='WBC COUNT:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=300+20+20+30)

label_name=Label(text='PLATLETS:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=330+20+20+30)

label_name=Label(text='HB:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=360+20+20+30)

label_name=Label(text='URIC ACID:',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=390+20+20+30)

label_name=Label(text='CHOLESTROL',font=('Times New Roman',15),fg='black')
label_name.place(x=50,y=420+20+20+30)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=190)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=220)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=250)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=280)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=310)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=340)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=370)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=400)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=430)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=460)

entry_name=Entry(w,bg='white',fg='black')
entry_name.place(x=250,y=490)




def fun_rep():
    ww=Tk()
    ww.title("FITNESS CALCULATOR")
    ww.geometry('700x400')
    c=Canvas(ww,width=700,height=400,bg='#e3e3e3')
    c.pack()
    label_name=Label(ww,text='REPORT',font=('Times New Roman',15),fg='black',bg='yellow')
    label_name.place(x=300,y=10)
    label_bmir=Label(ww,text='BMI(BODY MASS INDEX):',font=('Times New Roman',15),fg='black')
    label_bmir.place(x=50,y=50-10)

    label_bpr=Label(ww,text='BP ((High/Medium/Low)) :',font=('Times New Roman',15),fg='black')
    label_bpr.place(x=50,y=80+10-10)

    label_pulser=Label(ww,text='PULSE RATE (High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_pulser.place(x=50,y=110+20-10)

    label_rbcr=Label(ww,text='RBC COUNT(High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_rbcr.place(x=50,y=140+30-10)

    label_wbcr=Label(ww,text='WBC COUNT (High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_wbcr.place(x=50,y=170+40-10)

    label_platr=Label(ww,text='PLATLETS (High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_platr.place(x=50,y=200+50-10)

    label_hbr=Label(ww,text='HB (High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_hbr.place(x=50,y=230+60-10)

    label_uricr=Label(ww,text='URIC ACID (High/Medium/Low) :',font=('Times New Roman',15),fg='black')
    label_uricr.place(x=50,y=260+70-10)

    label_cholr=Label(ww,text='CHOLESTROL (High/Medium/Low):',font=('Times New Roman',15),fg='black')
    label_cholr.place(x=50,y=290+80-10)    


    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=40+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=80+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=120+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=160+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=200+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=240+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=280+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=320+5)

    entry_name=Entry(ww,bg='white',fg='black')
    entry_name.place(x=200*2,y=360+5)
    






button_rep=Button(w,text='GENERATE REPORT',font=('Times New Roman',17),command=fun_rep,bg='light blue',fg='white')
button_rep.place(x=500,y=460)



