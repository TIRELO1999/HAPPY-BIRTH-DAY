import tkinter as tk
import random

#pygame.mixer.music.play(-1)
colors_list=['Red','Blue','Green','Purple','Khaki','Yellow','Gray','Pink','Brown','White',
             'Black','Orange','Sky Blue','Light Green','Navy','Blueviolet','Rosybrown','Gold']
root=tk.Tk()
root.title("HAPPY BIRTHDAY TIRELO")
#root.resizable(height=False,width=False)
color=random.choice(colors_list)
padxx=35
padyy=5

def Change_color():
    global colors_list
    root.configure(background=random.choice(colors_list))
    Display()

def Display():
    global color

    btn1=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn2=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn3=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn4=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn5=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn6=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn7=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn8=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn9=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn10=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)

    #*********************************888
    btn11=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn12=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn13=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn14=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn15=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn16=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn17=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn18=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn19=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn20=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)


    #***************************************************
    btn21=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn22=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn23=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn24=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn25=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)

    #***************************************************
    btn26=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn27=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn28=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn29=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)
    color=random.choice(colors_list)
    btn30=tk.Button(root,text="",bg=color,padx=padxx,pady=padyy,borderwidth=1)

    btn_chng=tk.Button(root,text="change color",borderwidth=1,command=lambda :Change_color())
    color = random.choice(colors_list)
    text=tk.Label(root,text="HAPPY BIRTHDAY  TIRELO LESUFI".format(color),font=('Arial',25,'bold'),fg=color)

    btn_chng.grid(row=7,column=0,columnspan=10)
    text.grid(row=1,column=0,rowspan=5,columnspan=10)
    #display
    btn1.grid(row=0,column=0)
    btn2.grid(row=0,column=1)
    btn3.grid(row=0,column=2)
    btn4.grid(row=0,column=3)
    btn5.grid(row=0,column=4)
    btn6.grid(row=0,column=5)
    btn7.grid(row=0,column=6)
    btn8.grid(row=0,column=7)
    btn9.grid(row=0,column=8)
    btn10.grid(row=0,column=9)

    #------------
    btn11.grid(row=6,column=0)
    btn12.grid(row=6,column=1)
    btn13.grid(row=6,column=2)
    btn14.grid(row=6,column=3)
    btn15.grid(row=6,column=4)
    btn16.grid(row=6,column=5)
    btn17.grid(row=6,column=6)
    btn18.grid(row=6,column=7)
    btn19.grid(row=6,column=8)
    btn20.grid(row=6,column=9)

    #000000000000
    btn21.grid(row=1,column=0)
    btn22.grid(row=2,column=0)
    btn23.grid(row=3,column=0)
    btn24.grid(row=4,column=0)
    btn25.grid(row=5,column=0)
    #------
    btn26.grid(row=1,column=9)
    btn27.grid(row=2,column=9)
    btn28.grid(row=3,column=9)
    btn29.grid(row=4,column=9)
    btn30.grid(row=5,column=9)
Display()
def run():
    root.mainloop()

run()

