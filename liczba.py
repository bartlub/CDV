class Number:
    def __init__(self, value):
        print("Metoda init wywołana")
        self.value = value
    def wyzeruj(self):
        self.value = 0
    def ustaw(self, ustaw):
        self.value = ustaw

print("Zaimportowano moduł", __name__)
