# DOMINO

Définissez une classe **Domino()** qui permette d’instancier des objets simulant les pièces d’un
jeu de dominos. Le constructeur de cette classe initialisera les valeurs des points présents sur
les deux faces A et B du domino (valeurs par défaut = 0).

Deux autres méthodes seront définies :

* une méthode affiche_points() qui affiche les points présents sur les deux faces ;
* une méthode valeur() qui renvoie la somme des points présents sur les 2 faces.
Exemples d’utilisation de cette classe :

```

>>> d1 = Domino(2,6)
>>> d2 = Domino(4,3)
>>> d1.affiche_points()
face A : 2 face B : 6
>>> d2.affiche_points()
face A : 4 face B : 3
>>> print("total des points :", d1.valeur() + d2.valeur())
15
>>> liste_dominos = []
>>> for i in range(7):
...
liste_dominos.append(Domino(6, i))
>>> print(liste_dominos[3])
<__main__.Domino object at 0xb758b92c>

```