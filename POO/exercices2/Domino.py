class Domino :
    """
    Definitions de la classe Domino
    """


    def __init__(self, faceA = 0 , faceB = 0):
        self.faceA = faceA
        self.faceB = faceB
    
    def affiche_points(self):
        print("face A : {0} , face B : {1}".format(self.faceA, 
                                            self.faceB))

    def valeur(self):
        return self.faceA + self.faceB

if __name__ == "__main__":
    d1 = Domino(2, 6)
    d2 = Domino(4, 3)
    
    d1.affiche_points()

    print("total des points :", d1.valeur() + d2.valeur())


