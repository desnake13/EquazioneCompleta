
# classe
class EquazioneCompleta:
    # funzione per l'input
    def __init__(self):
        self.a = float(input("Inserisci a: "))
        if self.a == 0:
            print("Il coefficente a è uguale a 0.")
        else:
            self.b = float(input("Inserisci b: "))
            self.c = float(input("Inserisci c: "))
            self.delta = 0
            self.x1 = 0
            self.x2 = 0
            self.calcolaDelta()
            self.calcolaX()
    # funzione per calcolare il delta
    def calcolaDelta(self):
        self.delta = self.b**2-4*(self.a)*(self.c)
        print("Delta = " + str(self.delta))
    # funzione per calcolare le x
    def calcolaX(self):
        if self.delta >= 0:
            self.formulaA = (-self.b -(self.delta**0.5))
            self.formulaB = (-self.b +(self.delta**0.5))
            self.x1 = self.formulaA /(2*(self.a))
            self.x2 = self.formulaB /(2*(self.a))
            print("x1 = " + str(self.x1))
            print("x2 = " + str(self.x2))
        elif self.delta == 0:
            self.formulaC = (-self.b / (2*(self.a)))
            self.x1 = self.formulaC
            self.x2 = self.formulaC
            print("x1 = " + str(self.x1))
            print("x2 = " + str(self.x2))
        else:
            print("L'equazione è impossibile perchè il delta < 0 (minore di zero)")

equazione1 = EquazioneCompleta()