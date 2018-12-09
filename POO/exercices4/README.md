# Voiture 

Définissez une classe **Voiture()** qui permette d’instancier des objets reproduisant le
comportement de voitures automobiles. 

Le constructeur de cette classe initialisera les
attributs d’instance suivants, avec les valeurs par défaut indiquées:

> marque = ' Ford ' , couleur = ' rouge ' , pilote = ' personne ' ,  vitesse = 0 .

Lorsque l’on instanciera un nouvel objet Voiture(), on pourra choisir sa marque et sa couleur,
mais pas sa vitesse, ni le nom de son conducteur.

Les méthodes suivantes seront définies :
* choix_conducteur(nom) permettra de désigner (ou changer) le nom du conducteur.

* accelerer(taux, duree) permettra de faire varier la vitesse de la voiture. La variation de
vitesse obtenue sera égale au produit : taux × duree. Par exemple, si la voiture accélère au
taux de 1,3 m/s pendant 20 secondes, son gain de vitesse doit être égal à 26 m/s. Des taux
négatifs seront acceptés (ce qui permettra de décélérer). La variation de vitesse ne sera pas
autorisée si le conducteur est ’personne’.

* affiche_tout() permettra de faire apparaître les propriétés présentes de la voiture, c’est-à-
dire sa marque, sa couleur, le nom de son conducteur, sa vitesse.

Exemples d’utilisation de cette classe :

```
>>> a1 = Voiture( ' Peugeot ' , ' bleue ' )
>>> a2 = Voiture(couleur = ' verte ' )
>>> a3 = Voiture( ' Mercedes ' )
>>> a1.choix_conducteur( ' Roméo ' )
>>> a2.choix_conducteur( ' Juliette ' )
>>> a2.accelerer(1.8, 12)
>>> a3.accelerer(1.9, 11)
Cette voiture n ' a pas de conducteur !
>>> a2.affiche_tout()
Ford verte pilotée par Juliette, vitesse = 21.6 m/s.
>>> a3.affiche_tout()
Mercedes rouge pilotée par personne, vitesse = 0 m/s.

```