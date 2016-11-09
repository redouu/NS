import requests
import logging
import xmltodict
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox

xml_file = 'reisinfo.xml'  #variable aanmaken met het pad naar xml bestand
#defineren van de NS API authenticatie gegevens(gebruikersnaam en key)
api_pass = ('brahim.asdaou@student.hu.nl', 'KNZYQ_8TBr24vRmUm7UYUDDx_hz0ybxtAks_2_t5V1_eZvzwSM_RyQ')

def read_xml():  # functie read_xml defineren

def write_xml(reply, file):  # functie write_xml defineren
  bestand = open(file, 'w')  # bestand openen
  bestand.write(str(reply))  # bestand schrijven
  bestand.close()  # bestand afsluiten
  
# functie NS_API defineren met 2 parameters(reg, auth_details)

# functie station ophalen defineren

# functie station informatie ophalen defineren

# functie scherm_init() defineren om alle informatie en grafische objecten weer te geven.
# binnen de functie scherm_init() een andere functie defineren click()
# click functie wordt uitgevoerd zodra de gebuiker op de button klikt.
def scherm_init():
  scherm = Tk()
  scherm.wm_title("NS Reisinformatie")  # De Titel van het venseter scherm(verschijnt op de titelbalk)
  scherm.iconbitmap(r'ns.ico')  # Het icoontje toevoegen(verschijnt op de titelbalk)
  scherm.configure(background="#ffc917") # Achtergrond kleur
  scherm.attributes('-fullscreen', True)  # Volledig scherm

  def click(station): 
    if len(station) == 0: #als er niks is ingevuld
            msg = "Vul station in!" # melding defineren
            messagebox.showinfo(title="Melding", message=msg) #melding laten zien
    else:
  
scherm_init().mainloop() # om een loop te maken van de programma zodat deze constant wordt weergegeven
