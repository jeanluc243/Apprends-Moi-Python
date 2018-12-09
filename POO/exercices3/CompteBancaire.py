class CompteBancaire():
    """
    Gestion des Banques
    """
    
    def __init__(self, nom = 'Dupont', solde = 1000 ):
        """
        constructeur
        """

        self.nom   = nom
        self.solde = solde

    def depot(self, somme):
        """
        ajouter somme au solde
        """ 

        self.solde = self.solde + somme

    def retrait(self, somme):
        """
        retirer somme du solde
        """ 

        self.solde = self.solde - somme

    def affiche(self):
        print("Le compte bancaire de {0} est de {1} euros".format(
                                                self.nom , self.solde))
       

if __name__ == '__main__':
    compte1 = CompteBancaire('Duchmo1', 800)
    compte1.depot(350)
    compte1.retrait(200)
    compte1.affiche()
    
    