'''
  Name: Jack Morgan, and Tyler DeClifford
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal '''
# used to create a custom window for triangle calculator
import tkinter as tk
from math import sqrt

#                      FUNCTION





def get_sidec():
    # gets the three entries
    a = int(e_sidea.get())
    b =int(e_sideb.get())   
    c = sqrt(a**2 + b**2)

    tbox_c.config(state='normal')
  
    #age calculated is inserted into the text box after clearing the previous info in the text box
    
    tbox_c.delete('1.0', tk.END)
    tbox_c.insert(tk.END,c)
    tbox_c.config(state='disabled')
  
def display_calc_c():    
    tbox_c.config(state='normal')

    
    #c calculated is inserted into the text box after clearing the previous info in the textbox.

def display_calc_sidec(sidec):    
    tbox_c.config(state='normal')
   
    print("Input lengths of shorter triangle sides:")
    a = float(input("a: "))
    b = float(input("b: "))
    global c
    c = sqrt(a**2 + b**2)

    print("The length of the hypotenuse is:", c )

def exit():
    window.destroy()


  
  
  
#                      WINDOW MAIN
# Create a object which stores today's whole date using datetime function


# Creating a custom window

window = tk.Tk()
window.geometry("600x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Right Angle triangle solver')

#Labels for Heading and Subheading of GUI
lb_heading = tk.Label(window,text="Right Angle Triangle Solver",font=("Arial",20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your Triangle Side Values for Solving Hypotenuse Side!",fg="black",bg="#F7DC6F")

# labels for date, month and year
lb_sidea = tk.Label(window,text = "Side A: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

lb_sideb = tk.Label(window,text = "Side B: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")


# Entry boxes for date, month and year
e_sidea = tk.Entry(window,width=5)
e_sideb = tk.Entry(window,width=5)
#e_sidec = tk.Entry(window,width=5)

# Button to solve triangle
btn_calculate_sidec = tk.Button(window,text="Solve",font=("Arial",13), command=get_sidec)


lb_calculated_sidec = tk.Label(window,text="Side C = ",font=("Arial",12,"bold"),fg="darkgreen",bg="#F7DC6F") 
tbox_c=tk.Text(window,width=5,height=0,state="disabled")


btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)


lb_heading.place(x=110,y=5)
lb_subheading.place(x=80,y=40)
lb_sidea.place(x=160,y=90)
lb_sideb.place(x=160,y=120)
e_sidea.place(x=240,y=90)
e_sideb.place(x=240,y=120)
btn_calculate_sidec.place(x=180,y=150)
lb_calculated_sidec.place(x=160,y=200)
tbox_c.place(x=240,y=203)
btn_exit.place(x=115,y=230)