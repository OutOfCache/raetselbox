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

#draw.text((30, 20), "FPROG PRATKIKUM",fonst=FreeSans12, fill=1) #30 Pixel nach recht, 20 pixel nach unten
#draw.text((45, 30), "ROCKT! :D",fonst=FreeSans20, fill=1)
draw.text((30,20),"FPROG PRAKTIKUM",fill=1)
draw.text((45,30),"ROCKT! :D", fill=1)
# Ausgaben auf Display schreiben
oled.display()
