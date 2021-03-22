import json
import display
import random
import time

class Puzzle:
    

    def __init__(self, raetsel):
        """
        param - dictionary mit Raetseleigenschaften
        """
        self.__puzzle_text = raetsel["problemstellung"]
        # self.__puzzle_img = raetsel["puzzle_img"]
        self.__hints = raetsel["hinweise"]
        self.__temp = raetsel["temp"]
        self.__luft = raetsel["luft"]
        self.__hell = raetsel["hell"]
        self.__solved = raetsel["gelöst"]

        self.__used_hints = 0

    def __str__(self):
        s = '{0}\n{1}\n{2}\n{3}\n{4}'
        return s.format(self.__puzzle_text, self.__hints, self.__temp, self.__luft, self.__solved)

   


    def use_hint(self):
        display.display.print_text(self.__hints[self.__used_hints])
        self.__used_hints += 1

    
    def puzzle_complete(self):
        display.display.print_text(self.__solved)

    def puzzle_solve(self):
        #cur_temp = float(input("Temperatur: "))
        #cur_luft = float(input("Luftfeuchtigkeit: "))

        # für Demozwecke:
        cur_temp = random.random() * 100
        cur_luft = random.random() * 100
        cur_hell = random.random() * 100

        while cur_temp < self.__temp or cur_luft < self.__luft or cur_hell < self.__hell:
            # print("Leider falsch! Versuchs nochmal")
            time.sleep(10)
            cur_temp = self.__temp
            cur_luft = self.__luft
            cur_hell = self.__hell
            #use_hint = input("Hinweis verwenden? Y/N")
            #if use_hint == "Y" or "y":
            #    self.use_hint()
            #    yield False

        self.puzzle_complete()
        return True


    def puzzle_ask(self):
        #print(self.__puzzle_text)
        display.display.print_text(self.__puzzle_text)
        while not self.puzzle_solve():
            pass

        # gelöst
        return True

