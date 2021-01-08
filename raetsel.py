import json

class Puzzle:
    __used_hints = 0

    def __init__(self, raetsel):
        """
        param - dictionary mit Raetseleigenschaften
        """
        self.__puzzle_text = raetsel["problemstellung"]
        # self.__puzzle_img = raetsel["puzzle_img"]
        self.__hints = raetsel["hinweise"]
        self.__temp = raetsel["temp"]
        self.__luft = raetsel["luft"]
        self.__solved = raetsel["gelöst"]

    def __str__(self):
        s = '{0}\n{1}\n{2}\n{3}\n{4}'
        return s.format(self.__puzzle_text, self.__hints, self.__temp, self.__luft, self.__solved)

   


    def use_hint(self):
        print(self.__hints[Puzzle.__used_hints])
        Puzzle.__used_hints += 1

    
    def puzzle_complete(self):
        print(self.__solved)

    def puzzle_solve(self):
        cur_temp = float(input("Temperatur: "))
        cur_luft = float(input("Luftfeuchtigkeit: "))

        while cur_temp < self.__temp or cur_luft < self.__luft:
            print("Leider falsch! Versuchs nochmal")
            use_hint = input("Hinweis verwenden? Y/N")
            if use_hint == "Y" or "y":
                self.use_hint()
                yield False

        self.puzzle_complete()
        return True


    def puzzle_ask(self):
        print(self.__puzzle_text)
        while not self.puzzle_solve():
            pass

