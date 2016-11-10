import requests
import logging
import xmltodict
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox

xml_file = 'reisinfo.xml'
api_key = ('brahim.asdaou@student.hu.nl', 'KNZYQ_8TBr24vRmUm7UYUDDx_hz0ybxtAks_2_t5V1_eZvzwSM_RyQ')
root = Tk()
root.configure(background="#ffc917")
root.attributes('-fullscreen', True)
root.iconbitmap(r'ns.ico')
def esc(event):
        sys.exit()
root.bind('<Escape>', esc)
def lees_xml(file):
    bestand = open(file, 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)
def write_xml(reply, file):
    bestand = open(file, 'w')
    bestand.write(str(reply))
    bestand.close()
def request_xml(http, key):
    try:
        reply = requests.get(http, auth=key)
        return reply
    except:
        return logging.exception('')
      
# def station items
# def station info
def bg():
    bgc = Label(root, height=1000, width=1000, anchor=N, background="#ffc917")
    bgc.grid(row=0, column=0, sticky="nsew")
    return root
def info_init():
    root.wm_title("NS Reisinformatie")
    #  Tekstlabel weergeven
    infolabel = Label(root, text="Voer hieronder uw huidige station in om de actuele reistijden en overige reisinformatie op te vragen.", background="#ffc917", foreground="#003082", anchor=CENTER)
    infolabel.config(font=("Arial", 16))
    infolabel.place(relx=.5, rely=.02, anchor="center")
    #  Input weergeven
    input = Entry(root, width=42)
    input.config(font=("Arial", 16))
    input.place(relx=.5, rely=.05, anchor="center")
    #  Button weergeven en linken naar de click functie
    searchbutton = Button(root, text="Bekijk de actuele reisinformatie", background="#003082", foreground="white", command=lambda: click(input.get()), anchor=CENTER)
    searchbutton.config(font=("Arial", 16))
    searchbutton.place(relx=.5, rely=.09, anchor="center")
    def click(station):
        if len(station) == 0:
            msg = "Vul station in!"
            messagebox.showinfo(title="Melding", message=msg)
        else:
            if station:
                try:
                    msg = get_station_info(station)
                    infotext = Label(root, height=56, width=64, text=msg, anchor=N, font=("Arial", 10, "bold"), background="#ffffff")
                    infotext.place(relx=.5, rely=.54, anchor="center")
                except UserWarning as msg:
                    msg = 'Onjuiste Stationsnaam!'
                    messagebox.showinfo(title="Melding", message=msg)
            else:
                msg = 'Er is een fout opgetreden..'
                messagebox.showinfo(title="Melding", message=msg)
    return root
start_init().mainloop()
