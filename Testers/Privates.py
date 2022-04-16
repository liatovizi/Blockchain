
class Szemely:
    def __init__(self, nev, kor):
        self.__nev = nev
        self.kor = kor

    def get_nev(self):
        return self.__nev

sz = Szemely('E', 28)
print(sz.get_nev())
print(sz.kor)