#!/usr/bin/env python
# coding=utf-8
# Bibliotheken importieren
from lib_oled96 import ssd1306
from smbus import SMBus
# Display einrichten
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
# Ein paar Abkürzungen, um den Code zu entschlacken
draw = oled.canvas
#Schriftarten
#FreeSans12 = ImageFont.truetype('FreeSans.ttf',12)
#FreeSans20 = ImageFonst.truetype('FreeSans.ttf',20)

# Display zum Start löschen
oled.cls()
oled.display()

#draw.text((30, 20), "FPROG PRATKIKUM",fonst=FreeSans12, fill=1) #30 Pixel nach rechts, 20 pixel nach unten
#draw.text((45, 30), "ROCKT! :D",fonst=FreeSans20, fill=1)
#draw.text((30,20),"FPROG PRAKTIKUM",fill=1)
#draw.text((45,30),"ROCKT! :D", fill=1)
# Ausgaben auf Display schreiben


def print_text(text):
    # String auf Zeilen aufteilen
    zeilen = []
    n = 20  # max. Zeichenlänge
    last_index = 0
    end = False
    while(not end):
        if len(text[last_index:]) > n:
            index = text[last_index:last_index+n].rfind(" ")
            zeilen.append(text[last_index:index]) 
            last_index = index + 1
        else:
            zeilen.append(text[last_index:])
            end = True

    for i in range(len(zeilen)):
        draw.text((10, 10 * i)), zeilen[i])

    #oled.display()

print_text("FPROG PRAKTIKUM ROCKT! :D")