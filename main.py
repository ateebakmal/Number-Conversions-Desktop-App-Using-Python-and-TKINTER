import tkinter as tk
from tkinter import StringVar, ttk
import numbersystem




#Binary conversions functions   
def convert_decimal_to_binary():
    try:
         label_equation = text_box.get()
         answer = numbersystem.decimalToBinary(int(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct decimal value")

def convert_decimal_to_octal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.decimalToOctal(int(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct decimal value")

def convert_decimal_to_hexa():
    try:
         label_equation = text_box.get()
         answer = numbersystem.decimalToHexa(int(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct decimal value")

#----------------------------------------------------------------
#Making binary conversions functions
        
def convert_binary_to_decimal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.binaryToDecimal(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct binary value")     


def convert_binary_to_octal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.binaryToOctal(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct binary value") 

def convert_binary_to_hexa():
    try:
         label_equation = text_box.get()
         answer = numbersystem.binaryToHexa(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct binary value")    


#----------------------------------------------------------------
#Making octal conversions functions
def convert_octal_to_binary():
    try:
         label_equation = text_box.get()
         answer = numbersystem.octalToBinary(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct octal value")      

def convert_octal_to_decimal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.octalToDecimal(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct octal value")

def convert_octal_to_hexa():
    try:
         label_equation = text_box.get()
         answer = numbersystem.octalToHexa(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct octal value")

#----------------------------------------------------------------
#Making octal conversions functions  

def convert_hexa_to_binary():
    try:
         label_equation = text_box.get()
         answer = numbersystem.hexaToBinary(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct hexa value")

def convert_hexa_to_octal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.hexaToOctal(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct hexa value")     

def convert_hexa_to_decimal():
    try:
         label_equation = text_box.get()
         answer = numbersystem.hexaToDecimal(str(label_equation))
         equation_label.set(answer)
    except:
        equation_label.set("Please enter a correct hexa value")     

def clear():
    text_box.delete(0,len(text_box.get()))

WIDTH = 800
HEIGHT = 800
FONTNAME = "Times New Roman"

window = tk.Tk()

# Setting up window
window.title("Number Conversions by Ateeb")
window.geometry(f"{WIDTH}x{HEIGHT}")

#Making a label to show answers
equation_label = StringVar()
label = tk.Label(window,textvariable=equation_label,fg="Black",bg="beige",width=40,height=3,font=("Consolas",15))
label.pack(pady=20)

frame= tk.Frame(window)
frame.pack()

# Making buttons

#making decimal conversion buttons
decimal_to_binary_btn = tk.Button(frame,text="Decimal to Binary", font=(FONTNAME, 12), width=15, height=2,command=convert_decimal_to_binary)
decimal_to_binary_btn.grid(row= 5, column= 2,padx=10)

decimal_to_octal_btn = tk.Button(frame,text="Decimal to Octal", font=(FONTNAME, 12), width=15, height=2,command=convert_decimal_to_octal)
decimal_to_octal_btn.grid(row= 5, column= 3,padx=10)

decimal_to_hexa_btn = tk.Button(frame,text="Decimal to Hexa", font=(FONTNAME, 12), width=15, height=2,command=convert_decimal_to_hexa)
decimal_to_hexa_btn.grid(row= 5, column= 4,padx=10)


#making binary conversion buttons
frame.grid_rowconfigure(6,minsize=50)

binary_to_decimal_button = tk.Button(frame,text="Binary to Decimal", font=(FONTNAME, 12), width=15, height=2,command=convert_binary_to_decimal)
binary_to_decimal_button.grid(row= 7, column= 2,padx=10,pady=25)

binary_to_octal_button = tk.Button(frame,text="Binary to Octal", font=(FONTNAME, 12), width=15, height=2,command=convert_binary_to_octal)
binary_to_octal_button.grid(row= 7, column= 3,padx=10,pady=25)

binary_to_hexa_button = tk.Button(frame,text="Binary to Hexa", font=(FONTNAME, 12), width=15, height=2,command=convert_binary_to_hexa)
binary_to_hexa_button.grid(row= 7, column= 4,padx=10,pady=25)



#making octal conversion buttona
frame.grid_rowconfigure(8,minsize=50)

octal_to_binary_btn = tk.Button(frame,text="Octal to Binary", font=(FONTNAME, 12), width=15, height=2,command=convert_octal_to_binary)
octal_to_binary_btn.grid(row=9,column=2,padx=10)

octal_to_decimal_btn = tk.Button(frame,text="Octal to Decimal", font=(FONTNAME, 12), width=15, height=2,command=convert_octal_to_decimal)
octal_to_decimal_btn.grid(row=9,column=3,padx=10)

octal_to_hexa_btn = tk.Button(frame,text="Octal to Hexa", font=(FONTNAME, 12), width=15, height=2,command=convert_octal_to_hexa)
octal_to_hexa_btn.grid(row=9,column=4,padx=10)



#making hexa conversion buttons
frame.grid_rowconfigure(10,minsize=50)

hexa_to_binary_btn = tk.Button(frame,text="Hexa to Binary", font=(FONTNAME, 12), width=15, height=2,command= convert_hexa_to_binary)
hexa_to_binary_btn.grid(row=11,column=2,padx=10)

hexa_to_decimal_btn = tk.Button(frame,text="Hexa to Decimal", font=(FONTNAME, 12), width=15, height=2,command= convert_hexa_to_decimal)
hexa_to_decimal_btn.grid(row=11,column=3,padx=10)

hexa_to_octal_btn = tk.Button(frame,text="Hexa to Octal", font=(FONTNAME, 12), width=15, height=2,command= convert_hexa_to_octal)
hexa_to_octal_btn.grid(row=11,column=4,padx=10)


frame.grid_rowconfigure(12,minsize=50)

#adding a text box to input user
text_box = tk.Entry(frame,font=(FONTNAME, 17))
text_box.grid(row=13,column=3,padx=10,pady=10)

#adding a clear button
frame.grid_rowconfigure(14,minsize=50)
clear_button = tk.Button(frame,text="Clear", font=(FONTNAME, 12), width=15, height=1,command=clear)
clear_button.grid(row=15,column=3,pady=2)


window.mainloop()
