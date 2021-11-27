# Import module
import os
import tkinter
from tkinter import *
# Create object
from tkinter import ttk

import database
from dictionary import USTERKI, TIME
from report_generator import ReportGenerator

root = Tk()
db = database.InputDatabase("root", "")
report_service = ReportGenerator()

user = "default"
# Adjust size
root.geometry("1200x800")

# Add image file
bg = PhotoImage(file=fr"{os.getcwd()}\pivvo.png")

# Create Canvas
canvas1 = Canvas(root, width=1200, height=800)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")


def generuj_raport():
	if z_jak_dawna_raport.get():
		report_service.start(db=db, cursor=db.cursor, days=dni_rp.get(), supervisor=czyje_alarmy.get(),
							 time=TIME[z_jak_dawna_raport.get()], level=priorytet_raport.get())


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


# Create Buttons
button1 = Button(root, text=USTERKI[1], command=lambda: raise_allert(USTERKI[1], 1))
button2 = Button(root, text=USTERKI[2], command=lambda: raise_allert(USTERKI[2], 2))
button3 = Button(root, text=USTERKI[3], command=lambda: raise_allert(USTERKI[3], 3))
button4 = Button(root, text=USTERKI[4], command=lambda: raise_allert(USTERKI[4], 4))
button5 = Button(root, text=USTERKI[5], command=check_temperature_kadz)
button6 = Button(root, text=USTERKI[6], command=lambda: raise_allert(USTERKI[6], 6))
button7 = Button(root, text=USTERKI[7], command=lambda: raise_allert(USTERKI[7], 7))
button8 = Button(root, text=USTERKI[8], command=lambda: raise_allert(USTERKI[8], 8))
button9 = Button(root, text=USTERKI[9], command=check_temperature_fermentator)
button10 = Button(root, text=USTERKI[10], command=lambda: raise_allert(USTERKI[10], 10))
button11 = Button(root, text=USTERKI[11], command=lambda: raise_allert(USTERKI[11], 11))
button12 = Button(root, text=USTERKI[12], command=lambda: raise_allert(USTERKI[12], 12))
button13 = Button(root, text=USTERKI[13], command=lambda: raise_allert(USTERKI[13], 13))
button14 = Button(root, text=USTERKI[14], command=lambda: raise_allert(USTERKI[14], 14))
button15 = Button(root, text=USTERKI[15], command=lambda: raise_allert(USTERKI[15], 15))
button16 = Button(root, text=USTERKI[16], command=check_temperature_pasteryzator)
button17 = Button(root, text=USTERKI[17], command=lambda: raise_allert(USTERKI[17], 17))
button18 = Button(root, text=USTERKI[18], command=lambda: raise_allert(USTERKI[18], 18))

button1_canvas = canvas1.create_window(10, 10, anchor="nw", window=button1)  # brak jęczmienia
button2_canvas = canvas1.create_window(120, 40, anchor="nw", window=button2)  # usterka maszyny do zacieru
button3_canvas = canvas1.create_window(300, 40, anchor="nw", window=button3)  # usterka w młynie
button4_canvas = canvas1.create_window(440, 230, anchor="nw", window=button4)  # brak cieczy w kadzi do gotowania
button5_canvas = canvas1.create_window(440, 300, anchor="nw",
									   window=button5)  # ustaw temperaturę w zbiorniku do gotowania
button6_canvas = canvas1.create_window(470, 330, anchor="nw", window=button6)  # pęknięta kadź gotowania
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


def disable_all_buttons():
	button1["state"] = "disable"
	button2["state"] = "disable"
	button3["state"] = "disable"
	button4["state"] = "disable"
	button5["state"] = "disable"
	button6["state"] = "disable"
	button7["state"] = "disable"
	button8["state"] = "disable"
	button9["state"] = "disable"
	button10["state"] = "disable"
	button11["state"] = "disable"
	button12["state"] = "disable"
	button13["state"] = "disable"
	button14["state"] = "disable"
	button15["state"] = "disable"
	button16["state"] = "disable"
	button17["state"] = "disable"
	button18["state"] = "disable"


def enable_all_buttons():
	button1["state"] = NORMAL
	button2["state"] = "normal"
	button3["state"] = "normal"
	button4["state"] = "normal"
	button5["state"] = "normal"
	button6["state"] = "normal"
	button7["state"] = "normal"
	button8["state"] = "normal"
	button9["state"] = "normal"
	button10["state"] = "normal"
	button11["state"] = "normal"
	button12["state"] = "normal"
	button13["state"] = "normal"
	button14["state"] = "normal"
	button15["state"] = "normal"
	button16["state"] = "normal"
	button17["state"] = "normal"
	button18["state"] = "normal"


disable_all_buttons()


def sprawdz_logowanie():
	if db.check_user(userek=login.get(), passwordek=haslo.get()):
		enable_all_buttons()
		war_var.set("Zalogowano")
		global user
		user = login.get()
	else:
		war_var.set("Nieudane logowanie")


def raise_allert(incorrection_name: str, button_id: int = None):
	global user
	print(user)
	if not button_id:
		db.raise_allert(incorrection_name, user)
	else:
		db.raise_allert(USTERKI[button_id], user)


temperatura_pasteryzator = tkinter.Entry(root, state="normal")
temp1_canvas = canvas1.create_window(480, 640, anchor="nw", window=temperatura_pasteryzator)

temperatura_zbiornik_gotowania = tkinter.Entry(root, state="normal")
temp2_canvas = canvas1.create_window(500, 280, anchor="nw", window=temperatura_zbiornik_gotowania)

temperatura_w_fermentatorze = tkinter.Entry(root, state="normal")  # temperatura w fermentatorze
temp3_canvas = canvas1.create_window(10, 500, anchor="nw", window=temperatura_w_fermentatorze)

login = tkinter.Entry(root, state="normal")
haslo = tkinter.Entry(root, state="normal", show="*")
login_canvas = canvas1.create_window(800, 20, anchor="nw", window=login)
haslo_canvas = canvas1.create_window(950, 20, anchor="nw", window=haslo)

label_var = tkinter.StringVar()
label_var.set("Login")
login_label = ttk.Label(root, textvariable=label_var)

haslo_var = tkinter.StringVar()
haslo_var.set("Hasło")
haslo_label = ttk.Label(root, textvariable=haslo_var)

war_var = tkinter.StringVar()
war_var.set("")
warning_label = ttk.Label(root, textvariable=war_var)

dni_do_raportu = tkinter.StringVar()
dni_do_raportu.set("Raport z poprzednich X dni")
dni_label = ttk.Label(root, textvariable=dni_do_raportu)

login_label_canvas = canvas1.create_window(800, 40, anchor="nw", window=login_label)
haslo_label_canvas = canvas1.create_window(950, 40, anchor="nw", window=haslo_label)
warning_label_canvas = canvas1.create_window(800, 60, anchor="nw", window=warning_label)
dni_do_raportu_cansas = canvas1.create_window(990, 130, anchor="nw", window=dni_label)

dni_rp = tkinter.Entry(root, state="normal")
dni_rp_canvas = canvas1.create_window(1000, 150, anchor="nw", window=dni_rp)

z_jak_dawna_raport = ttk.Combobox(root, state="normal")
z_jak_dawna_raport["values"] = ("1 dzień", "1 tydzień", "1 miesiąc", "Ręczne ustawienia")
czas_raport_cnv = canvas1.create_window(800, 150, anchor="nw", window=z_jak_dawna_raport)

czyje_alarmy = ttk.Combobox(root, state="normal")
users = db.get_users_list()
czyje_alarmy["values"] = users
czyje_alarmy_raport_cnv = canvas1.create_window(800, 180, anchor="nw", window=czyje_alarmy)

priorytet_raport = ttk.Combobox(root, state="normal")
priorytet_raport["values"] = ("Normal", "Urgent", "Critical")
priorytet_raport_cnv = canvas1.create_window(800, 210, anchor="nw", window=priorytet_raport)

LOGUJ_BTN = Button(root, text="ROZPOCZNIJ PRACĘ", command=sprawdz_logowanie)
loguj_btn_cnv = canvas1.create_window(950, 70, anchor="nw", window=LOGUJ_BTN)

CREATE_REPORT_BUTTON = Button(root, text="Wygeneruj raport", command=generuj_raport)
report_btn_cnv = canvas1.create_window(950, 200, anchor="nw", window=CREATE_REPORT_BUTTON)

root.mainloop()
