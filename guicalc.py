#gui calculator
##################################################################
#getting set up
import threading, random
from threading import Thread
import time
import sys
import tkinter
import msvcrt
import os
import math
from tkinter import *
#####################################################################
#TYPE!!! yourself!!!
x=''
zeta=''
def input():
    global x
    global zeta
    m=4
    while m>0:
        a=msvcrt.getch()
        a=str(a)
        a=a[2:-1]
        x=x+a
        zeta=zeta+a
        display(zeta)
        print("you pressed ",a)
        time.sleep(0.075)
def window():
    global x
    global zeta
    ##################################################################
    alpha=Tk()
    alpha.configure(background='#00B88A')
    alpha.title("Sid's Friendly GUI Calc")
    alpha.geometry('410x480+210+35')
    alpha.resizable(width=FALSE, height=FALSE)
    #false=Button(alpha,text='',height=3,width=15).pack()
    ##################################################################
    #graphical coordinates fix
    xfix=-150
    yfix=-200

    #################################################################################
    #menu functions  (INCOMPLETE)
    def mbox():
        m=5
    def iwqut():
        alpha.destroy()
    def mrestart():
        m=5
    def cclr():
        m=5
    #######################################################################################################
    #Menu Construction
    mnu=Menu(alpha)
    filemenu = Menu(mnu,tearoff=0)
    filemenu.add_command(label="Edit")
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Help",command=mbox)
    filemenu.add_command(label="Exit",command=iwqut)
    mnu.add_cascade(label="File",menu=filemenu)

    mnu2=Menu(alpha)
    filemenu2 = Menu(mnu2,tearoff=0)
    filemenu2.add_command(label="Volume")
    filemenu2.add_command(label="Emoticon")
    filemenu2.add_command(label="Restart",command=mrestart)
    filemenu2.add_command(label="Color", command = cclr)

    mnu.add_cascade(label="Options",menu=filemenu2)
    alpha.config(menu=mnu)
    ###############################################################################
    #fonts
    #incomplete
    #####################################################################
    #calculations for when '=' is pressed
    def calculations():
        global zeta
        global x
        try:
            z=zeta
            x=eval(x)
            if int(x)==x:
                x=int(x)
            x=round(x,5)
            idisplay("Calculating...")
            edisplay("【・_・?】")
            wait(0.05)
            x=str(x)
            y=z+"="+x
            display(y)
            idisplay("Done!")
            edisplay("(☆^ー^☆)")
            zeta=x
        except:
            x=''
            display("?")
            
            errordisplay("Error")
           
            edisplay("(✖╭╮✖)")
    ##################################################################
    #wait thread,  not complete, unexpected outcome currently
    def wait(x):
        time.sleep(x)
    ##################################################################
    #display thread   main display box for expression/answer
    def mdisplay(x):
        global zeta
        display_label=Button(alpha,text=x,height=4,width=35,font=60,command = calculations,bg='white').place(x=195+xfix,y=20)
       # time.sleep(0)
       # sys.stdout.flush()
    def ndisplay(x):
       # global x
       # sys.stdout.flush()
        display_label=Button(alpha,text=x,height=4,width=35,font=60,command = calculations,bg='#9CE1F2').place(x=195+xfix,y=20)
    def display(x):
        mdisplay(x)
        wait(0.05)
        ndisplay(x)
    ##################################################################

    #information box   secondary box that displays hints and solves currently entered in expression
    def errordisplay(x):
        display_label=Button(alpha,text=x,height=4,width=22,font=60,command = calculations,bg='#9CE1F2',fg='red').place(x=195+xfix,y=110)    
    def idisplay(x):
        display_label=Button(alpha,text=x,height=4,width=22,font=60,command = calculations,bg='#9CE1F2').place(x=195+xfix,y=110)
    idisplay('calculating...')
    #Friendly box   emoticons
    def edisplay(x):
        display_label=Button(alpha,text=x,height=4,width=12,font=60,command = calculations,bg='#9CE1F2').place(x=252.5,y=110)
    edisplay('( ^_^)／')
    idisplay("Ready to Start")
    ##################################################################
    #default function for information box    partial expression simplifier
    def default(x):
        try:
            y=eval(x)
            if y>0:
                edisplay("( ^_^)／")
                
            if y<0:
                
                edisplay("(~‾⌣‾)~")
            elif (round(y,2))!=y:
                edisplay("(・_・ヾ")
            else:
                edisplay("(^0^)")
            idisplay(y)
        except:
            if x=="":
                idisplay("")
                edisplay("〜(^∇^〜)")
            else:
                idisplay("")
                edisplay("(T_T)")
    ##################################################################
    #setting up variables for program
            
    zeta=''
    #zeta is the text aspect of the expression the user has entered in
    x='Enter Any Key To Start'
    #x is the mathematical aspect of the expression the user has entered in

    y=0
    #y and z are not implimented yet
    z=0

    #display Enter Any Key to Start and dissapear once something is pressed
    display(x)
    x=''


    ##################################################################
    #defining functions for calculator

    #numbers 0-9   will simplify into 1 generic function later
    def c_1():
        global x
        global zeta
        x=x+'1'
        zeta=zeta+'1'
        display(zeta)
        default(x)
    def c_2():
        global x
        global zeta
        x=x+'2'
        zeta=zeta+'2'
        display(zeta)
        default(x)
    def c_3():
        global x
        global zeta
        x=x+'3'
        zeta=zeta+'3'
        display(zeta)
        default(x)
    def c_4():
        global x
        global zeta
        x=x+'4'
        zeta=zeta+'4'
        display(zeta)
        default(x)
    def c_5():
        global x
        global zeta
        x=x+'5'
        zeta=zeta+'5'
        display(zeta)
        default(x)
    def c_6():
        global x
        global zeta
        x=x+'6'
        zeta=zeta+'6'
        display(zeta)
        default(x)
    def c_7():
        global x
        global zeta
        x=x+'7'
        zeta=zeta+'7'
        display(zeta)
        default(x)
    def c_8():
        global x
        global zeta
        x=x+'8'
        zeta=zeta+'8'
        display(zeta)
        default(x)
    def c_9():
        global x
        global zeta
        x=x+'9'
        zeta=zeta+'9'
        display(zeta)
        default(x)
    def c_0():
        global x
        global zeta
        x=x+'0'
        zeta=zeta+'0'
        display(zeta)
        default(x)

    ####################################################################
    #other defs
        
    #clears whatever is the current value of x and zeta
    def clear():
        global x
        global zeta
        x=''
        zeta=''
        display('')
        default(x)
    #addition
    def c_plus():
        global x
        global zeta
        x=x+'+'
        zeta=zeta+'+'
        display(zeta)
        default(x)
    #subtraction
    def c_minus():
        global x
        global zeta
        x=x+'-'
        zeta=zeta+'-'
        display(zeta)
        default(x)
    #multiplication
    def c_x():
        global x
        global zeta
        zeta=zeta+'×'
        x=x+'*'
        display(zeta)
        default(x)
    #you get the idea
    def c_div():
        global x
        global zeta
        zeta=zeta+'÷'
        x=x+'/'
        display(zeta)
        default(x)
    #button to exit program
    def Exit():
        alpha.destroy()
        sys.exit
    #backspace or delete button
    #index in a dictionary for deleting values
    def back():
        global x
        global zeta
        if zeta[-1]=="√":
            zeta=zeta[0:-1]
            x=x[0:-9]
        try:
            if x[-1]=='*' and x[-2]=='*':
                x=x[0:-2]
                zeta=zeta[0:-1]
        except:
            o=1
        else:
            x=x[0:-1]
            zeta=zeta[0:-1]
        display(zeta)
        default(x)
    #make a decimal
    def dec():
        global x
        global zeta
        x=x+'.'
        zeta=zeta+'.'
        display(zeta)
        default(x)
    #show more buttons
    def more():
        edisplay("!!!(◕ o ◕)!!!")
        idisplay("More Buttons!")
        alpha.geometry('850x480+210+35')
    #show less buttons
    def less():
        edisplay("!!!(◕ o ◕)!!!")
        idisplay("Less Buttons!")
        alpha.geometry('410x480+350+35')
    #right parenthesis
    def rht():
        global x
        global zeta
        x=x+')'
        zeta=zeta+')'
        display(zeta)
        default(x)
    #left parenthesis
    def lft():
        global x
        global zeta
        x=x+'('
        zeta=zeta+'('
        display(zeta)
        default(x)
    #logorithmn function, not implimented
    def log():
        global x
        global zeta
        x=x+"math.log10("
        zeta=zeta+'log₁₀('
        display(zeta)
        default(x)
    #raise something to a power. ex. 2^3
    def power():
        global x
        global zeta
        zeta=zeta+'^'
        x=x+'**'
        display(zeta)
        default(x)
    #help button, incomplete
    def _help():
        idisplay("No help available right now")
        edisplay(":P")
    def func():
        global x
        global zeta
        zeta=zeta+"f(x)="
        display(zeta)
        #idisplay("Don't press =")
        default(x)
    def c_sqr():
        global x
        global zeta
        zeta=zeta+"²"
        x=x+"**2"
        display(zeta)
        default(x)
    def c_sqrt():
        global x
        global zeta
        zeta=zeta+"√("
        x=x+"math.sqrt("
        display(zeta)
        default(x)
    def graph():
        global x
        global zeta
    def c_var():
        global x
        global zeta
        zeta=zeta+"x"
        x=x+"x"
        display(zeta)
        default(x)
    def c_pi():
        global x
        global zeta
        zeta=zeta+"π"
        x=x+str(round(math.pi,4))
        display(zeta)
        default(x)
    def more_trig():
        edisplay("L(・o・)」")
        idisplay("Trig Functions+etc!")
        alpha.geometry('850x640+170+25')
    def less_trig():
        edisplay("L(・o・)」")
        idisplay("Back to Normal!")
        alpha.geometry('850x480+210+35')
    def c_sin():
        global x
        global zeta
        x=x+"math.sin((math.pi/180)*"
        zeta=zeta+"sin("
        display(zeta)
        default(x)
    ####################################################################
    #adding number buttons for calculator
    button_1=Button(alpha,text='1',command = c_1,height=3,width=5).place(x=300+xfix,y=200)
    button_2=Button(alpha,text='2',command = c_2,height=3,width=5).place(x=350+xfix,y=200)
    button_3=Button(alpha,text='3',command = c_3,height=3,width=5).place(x=400+xfix,y=200)
    button_4=Button(alpha,text='4',command = c_4,height=3,width=5).place(x=300+xfix,y=260)
    button_5=Button(alpha,text='5',command = c_5,height=3,width=5).place(x=350+xfix,y=260)
    button_6=Button(alpha,text='6',command = c_6,height=3,width=5).place(x=400+xfix,y=260)
    button_7=Button(alpha,text='7',command = c_7,height=3,width=5).place(x=300+xfix,y=320)
    button_8=Button(alpha,text='8',command = c_8,height=3,width=5).place(x=350+xfix,y=320)
    button_9=Button(alpha,text='9',command = c_9,height=3,width=5).place(x=400+xfix,y=320)
    button_0=Button(alpha,text='0',command = c_0,height=3,width=5).place(x=350+xfix,y=380)
    ####################################################################
    #other buttons                                                                     
    button_plus=Button(alpha,text='+',command = c_plus,height=3,width=5).place(x=475+xfix,y=200)
    button_minus=Button(alpha,text='-',command = c_minus,height=3,width=5).place(x=475+xfix,y=260)
    button_x=Button(alpha,text='×',command = c_x,height=3,width=5).place(x=475+xfix,y=320)
    button_div=Button(alpha,text='÷',command = c_div,height=3,width=5).place(x=475+xfix,y=380)


    button_eval=Button(alpha,text='=',command=calculations,height=3,width=5).place(x=400+xfix,y=380)
    button_dec=Button(alpha,text='.',command=dec,height=3,width=5).place(x=300+xfix,y=380)
    button_back=Button(alpha,text='Delete',command=back,height=3,width=10).place(x=195+xfix,y=200)
    button_clear=Button(alpha,text='Clear',command=clear,height=3,width=10).place(x=195+xfix,y=260)
    button_exit=Button(alpha,text='Exit',command=Exit,height=3,width=10).place(x=195+xfix,y=320)
    button_more=Button(alpha,text='More',command=more,height=3,width=10).place(x=195+xfix,y=380)
    button_mtrig=Button(alpha,text='Trig',command=more_trig,height=3,width=6).place(x=490,y=170+120)
    button_ltrig=Button(alpha,text=' ↑ ',command=less_trig,height=3,width=6).place(x=430,y=170+320)
    #####################################################################
    #more buttons
    button_lftprnthsis=Button(alpha,text='(',command=lft,height=3,width=6).place(x=430,y=110)
    button_rghtprnthsis=Button(alpha,text=')',command=rht,height=3,width=6).place(x=490,y=110)
    button_power=Button(alpha,text='^',command=power,height=3,width=6).place(x=430,y=170)
    button_log=Button(alpha,text='log₁₀',command=log,height=3,width=6).place(x=490,y=170)
    button_less=Button(alpha,text='Less',command=less,height=3,width=6).place(x=430,y=50)
    button_help=Button(alpha,text='Help',command=_help,height=3,width=6).place(x=490,y=50)
    button_sqr=Button(alpha,text='x²',command=c_sqr,height=3,width=6).place(x=490,y=170+60)
    button_sqrt=Button(alpha,text='√x',command=c_sqrt,height=3,width=6).place(x=430,y=170+60)
    button_pi=Button(alpha,text='π',command=c_pi,height=3,width=6).place(x=430,y=170+120)
    ######################################################################
    #EVEN MORE BUTTONS
    button_func=Button(alpha,text="f(x)=",command=func,height=3,width=8).place(x=600,y=50)
    button_switch=Button(alpha,text="Graph function",command=graph, height=3,width=15).place(x=690,y=50)
    button_var=Button(alpha,text="x",command=c_var, height=3,width=15).place(x=690,y=120)
    coordlist=[]
    more()
    #########################################################################
    #trig buttons
    button_sin=Button(alpha,text='sin',command = c_sin,height=3,width=5).place(x=350,y=170+320)
###############################################################################
#restart program (ie. to use graph again)
    def rest():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        if __name__=="__main__":
            answer = input("Do you want to restart this program ? ")
            if answer.lower().strip() in "y yes".split():
                restart_program()
    #canvus_1 = Canvas(alpha,height=270,width=230,bg='green')
#############################################################################
#graphing function
    def grapher():
        try:
            canvus_1.destroy()
        except:
            pass
        canvus_1 = Canvas(alpha,height=230,width=230,bg='white')
        global x
        global zeta
        factor=64
        for t in range(0,(231*factor)):
            
            y=list(x)
#############################################################################
            #replace x's with values
            for ment in range(1,len(y)):
                if y[ment]=="x":
                    if y[ment-1].isdigit()==True:
                        y.insert(ment,"*")
            #if t<20:    
                #print(y)
            #change x's into t's
            for i in range(0,len(y)):
                if y[i]=="x":
                    
                    ban=str(((t)-115))
                    
                    
                    ban=float(ban)
                    if ban<0:   
                        y[i]=(str(ban))
                        y.insert(i,"(")
                        y.insert(i+2,")")
                    else:
                        y[i]=str(ban)
                    
            y=''.join(y)

            y=str(y)
#############################################################################
            #plug in for the given values 
            try:
                #IMPORTANT VERTICAL STRETCH IS WHATEVER multiplies eval(y)
                d=(eval(y)*1)+(230/2)
                
                
                int(d)
                d=d
            
                d=(230-(d))
                str(d)
                #IMPORTANT HORIZONTAL STRETCH IS WHATEVER MULTIPLIES "t"
                coordlist.append(t)
                coordlist.append(d)
            except:
                pass
################################################################################
        #make points (microscopic lines) on the canvas to graph the solution
        for i in range(0,231):
            try:
                canvus_1.create_line(coordlist[(2*i)],coordlist[(2*i)+1],(coordlist[2*i]+1),(coordlist[(2*i)+1]+1))
            except:
                global zeta
###################################################################################
        #x and y axis
        canvus_1.create_line((230/2),0,(230/2),230)
        canvus_1.create_line(0,(230/2),230,(230/2))
        #############################
        #creating the canvas
        canvus_1.place(x=580,y=200)
        edisplay("(☆^ー^☆)")
        idisplay("Graphed!")
######################################################################################
    button_switch=Button(alpha,text="Graph function",command=grapher, height=3,width=15).place(x=690,y=50)
    button_restart=Button(alpha,text="Reset",command=rest, height=3,width=8).place(x=600,y=60+60)
    #########################################################################
    #needed to run function
    alpha.mainloop()
def Main():
    t1 = Thread(target=input)
    t2 = Thread(target=window)
    t2.start()
    #t1.start()
if __name__ == '__main__':
    Main()
