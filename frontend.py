# Import module
import tkinter
from tkinter import *

# Create object
from dictionary import USTERKI
import env

root = Tk()

def raise_allert(incorrection_name: str):
	print(f"Temperature is too {incorrection_name}")


def check_temperature():
	if int(temperatura.get()) > 50:
		raise_allert("high")
	elif int(temperatura.get()) < 10:
		raise_allert("low")

# Adjust size
root.geometry("1200x500")

# Add image file
bg = PhotoImage(file=r"C:\Users\marta\Desktop\pivvo.png")

# Create Canvas
canvas1 = Canvas(root, width=400,
				 height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
					 anchor="nw")

# Add Text
canvas1.create_text(200, 250, text="Welcome")

# Create Buttons
button1 = Button(root, text=USTERKI[1])
button3 = Button(root, text=USTERKI[2])
button2 = Button(root, text=USTERKI[3])
button4 = Button(root, text=USTERKI[4])
button5 = Button(root, text=USTERKI[5])
button6 = Button(root, text=USTERKI[6])
button7 = Button(root, text=USTERKI[7])
button8 = Button(root, text=USTERKI[8])
button9 = Button(root, text=USTERKI[9])
button10 = Button(root, text=USTERKI[10])
button11 = Button(root, text=USTERKI[11])
button12 = Button(root, text=USTERKI[12])
button13 = Button(root, text=USTERKI[13])
button14 = Button(root, text=USTERKI[14])
button15 = Button(root, text=USTERKI[15])
button16 = Button(root, text=USTERKI[16], command=check_temperature)
button17 = Button(root, text=USTERKI[17])
button18 = Button(root, text=USTERKI[18])

# Display Buttons
button1_canvas = canvas1.create_window(100, 10, anchor="nw", window=button1)
button2_canvas = canvas1.create_window(100, 40, anchor="nw", window=button2)
button3_canvas = canvas1.create_window(100, 70, anchor="nw", window=button3)
button4_canvas = canvas1.create_window(100, 90, anchor="nw", window=button4)
button5_canvas = canvas1.create_window(100, 110, anchor="nw", window=button5)
button6_canvas = canvas1.create_window(100, 130, anchor="nw", window=button6)
button7_canvas = canvas1.create_window(100, 150, anchor="nw", window=button7)
button8_canvas = canvas1.create_window(100, 170, anchor="nw", window=button8)
button9_canvas = canvas1.create_window(100, 190, anchor="nw", window=button9)
button10_canvas = canvas1.create_window(100, 210, anchor="nw", window=button10)
button11_canvas = canvas1.create_window(100, 230, anchor="nw", window=button11)
button12_canvas = canvas1.create_window(100, 250, anchor="nw", window=button12)
button13_canvas = canvas1.create_window(100, 270, anchor="nw", window=button13)
button14_canvas = canvas1.create_window(100, 290, anchor="nw", window=button14)
button15_canvas = canvas1.create_window(100, 310, anchor="nw", window=button15)

temperatura = tkinter.Entry(root, state="normal")
temp_canvas = canvas1.create_window(170, 330, anchor="nw", window=temperatura)
button16_canvas = canvas1.create_window(100, 330, anchor="nw", window=button16)

button17_canvas = canvas1.create_window(100, 350, anchor="nw", window=button17)
button18_canvas = canvas1.create_window(100, 370, anchor="nw", window=button18)


# Execute tkinter
root.mainloop()
