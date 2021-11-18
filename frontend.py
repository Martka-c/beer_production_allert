# Import module
import tkinter
from tkinter import *

# Create object
import database
from dictionary import USTERKI


root = Tk()
db = database.InputDatabase("root", "")
user = "default"
def raise_allert(incorrection_name: str, button_id: int = None):
	if button_id not in [5, 9, 16]:
		db.raise_allert(incorrection_name, user)
	else:
		db.raise_allert(USTERKI[button_id], user)


def check_temperature_pasteryzator():
	if temperatura_pasteryzator.get():
		if int(temperatura_pasteryzator.get()) > 50:
			raise_allert("Zbyt wysoka temperatura w pasteryzatorze")
		elif int(temperatura_pasteryzator.get()) < 10:
			raise_allert("Zbyt niska temperatura w pasteryzatorze")


def check_temperature_fermentator():
	if temperatura_w_fermentatorze.get():
		if int(temperatura_w_fermentatorze.get()) > 50:
			raise_allert("Zbyt wysoka temperatura w fermentatorze")
		elif int(temperatura_w_fermentatorze.get()) < 10:
			raise_allert("Zbyt niska temperatura w fermentatorze")


def check_temperature_kadz():
	if temperatura_zbiornik_gotowania.get():
		if int(temperatura_zbiornik_gotowania.get()) > 50:
			raise_allert("Zbyt wysoka temperatura w zbiorniku do gotowania")
		elif int(temperatura_zbiornik_gotowania.get()) < 10:
			raise_allert("Zbyt niska temperatura w zbiorniku do gotowania")


# Adjust size
root.geometry("1200x800")

# Add image file
bg = PhotoImage(file=r"C:\Users\marta\Desktop\pivvo.png")

# Create Canvas
canvas1 = Canvas(root, width=1200, height=800)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Create Buttons
button1 = Button(root, text=USTERKI[1], command=lambda: raise_allert(USTERKI[1], 1))
button2 = Button(root, text=USTERKI[2], command=lambda: raise_allert(USTERKI[2], 1))
button3 = Button(root, text=USTERKI[3], command=lambda: raise_allert(USTERKI[3], 1))
button4 = Button(root, text=USTERKI[4], command=lambda: raise_allert(USTERKI[4], 1))
button5 = Button(root, text=USTERKI[5], command=check_temperature_kadz)
button6 = Button(root, text=USTERKI[6], command=lambda: raise_allert(USTERKI[6], 1))
button7 = Button(root, text=USTERKI[7], command=lambda: raise_allert(USTERKI[7], 1))
button8 = Button(root, text=USTERKI[8], command=lambda: raise_allert(USTERKI[8], 1))
button9 = Button(root, text=USTERKI[9], command=check_temperature_fermentator)
button10 = Button(root, text=USTERKI[10], command=lambda: raise_allert(USTERKI[10], 1))
button11 = Button(root, text=USTERKI[11], command=lambda: raise_allert(USTERKI[11], 1))
button12 = Button(root, text=USTERKI[12], command=lambda: raise_allert(USTERKI[12], 1))
button13 = Button(root, text=USTERKI[13], command=lambda: raise_allert(USTERKI[13], 1))
button14 = Button(root, text=USTERKI[14], command=lambda: raise_allert(USTERKI[14], 1))
button15 = Button(root, text=USTERKI[15], command=lambda: raise_allert(USTERKI[15], 1))
button16 = Button(root, text=USTERKI[16], command=check_temperature_pasteryzator)
button17 = Button(root, text=USTERKI[17], command=lambda: raise_allert(USTERKI[17], 1))
button18 = Button(root, text=USTERKI[18], command=lambda: raise_allert(USTERKI[18], 1))

# Display Buttons
button1_canvas = canvas1.create_window(10, 10, anchor="nw", window=button1) # brak jęczmienia
button2_canvas = canvas1.create_window(120, 40, anchor="nw", window=button2) # usterka maszyny do zacieru
button3_canvas = canvas1.create_window(300, 40, anchor="nw", window=button3) # usterka w młynie
button4_canvas = canvas1.create_window(440, 230, anchor="nw", window=button4) #brak cieczy w kadzi do gotowania
button5_canvas = canvas1.create_window(440, 300, anchor="nw", window=button5) #ustaw temperaturę w zbiorniku do gotowania
button6_canvas = canvas1.create_window(470, 330, anchor="nw", window=button6) # pęknięta kadź gotowania
button7_canvas = canvas1.create_window(110, 370, anchor="nw", window=button7)
button8_canvas = canvas1.create_window(30, 420, anchor="nw", window=button8)
button9_canvas = canvas1.create_window(20, 450, anchor="nw", window=button9)
button10_canvas = canvas1.create_window(10, 560, anchor="nw", window=button10)
button11_canvas = canvas1.create_window(10, 650, anchor="nw", window=button11)
button12_canvas = canvas1.create_window(510, 500, anchor="nw", window=button12)
button13_canvas = canvas1.create_window(530, 530, anchor="nw", window=button13)
button14_canvas = canvas1.create_window(510, 560, anchor="nw", window=button14)
button15_canvas = canvas1.create_window(480, 600, anchor="nw", window=button15)
button16_canvas = canvas1.create_window(480, 660, anchor="nw", window=button16)
button17_canvas = canvas1.create_window(250, 720, anchor="nw", window=button17)
button18_canvas = canvas1.create_window(410, 720, anchor="nw", window=button18)

temperatura_pasteryzator = tkinter.Entry(root, state="normal")
temp1_canvas = canvas1.create_window(480, 640, anchor="nw", window=temperatura_pasteryzator)

temperatura_zbiornik_gotowania = tkinter.Entry(root, state="normal")
temp2_canvas = canvas1.create_window(500, 280, anchor="nw", window=temperatura_zbiornik_gotowania)

temperatura_w_fermentatorze = tkinter.Entry(root, state="normal") #temperatura w fermentatorze
temp3_canvas = canvas1.create_window(10, 500, anchor="nw", window=temperatura_w_fermentatorze)


# Execute tkinter
root.mainloop()
