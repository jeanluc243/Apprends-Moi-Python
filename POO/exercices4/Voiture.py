class Voiture :
    """
    comportement de voitures automobiles
    """

    def __init__(self, marque = 'Ford', couleur = 'rouge'):
        
        self.marque  = marque
        self.couleur = couleur
        self.pilote  = 'personne'
        self.vitesse = 0

    def choix_conducteur(self,nom):
        """
        permet de designer(ou changer ) le nom du conducteur
        """

        self.pilote = nom

    def accelerer(self, taux, duree):
        """
        permet de faire varier la vitesse de la voiture
        """

        if self.pilote == 'personne':
            print("Cette voiture n'a pas de conducteur !")
        else :

            self.vitesse = taux * duree

    def affiche_tout(self):
        print("{0} {1} pilotée par {2} , vitesse = {3} m/s".format(self.marque,
                                            self.couleur, self.pilote, self.vitesse))


if __name__ == '__main__':
    a1 = Voiture('Peugeot', 'bleue')
    a2 = Voiture(couleur='verte')
    a3 = Voiture('Mercedes')
    a1.choix_conducteur('Roméo')
    a2.choix_conducteur('Juliette')
    a2.accelerer(1.8, 12)
    a3.accelerer(1.9, 11)
    a2.affiche_tout()
    a3.affiche_tout()
    