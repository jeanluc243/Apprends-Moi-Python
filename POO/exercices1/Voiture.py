class Voiture :
    
    vitesse = 0

    def incrementer(self, nbreVitesse):
        self.vitesse = nbreVitesse

    def decrementer(self, nbreVitesse):
        self.vitesse = nbreVitesse

if __name__ == "__main__":
    prado = Voiture()
    prado.incrementer(40)
    
