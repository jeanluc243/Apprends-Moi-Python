# Satellite 


Définissez une classe **Satellite()** qui permette d’instancier des objets simulant des satellites
artificiels lancés dans l’espace, autour de la terre. Le constructeur de cette classe initialisera
les attributs d’instance suivants, avec les valeurs par défaut indiquées :

> masse = 100, vitesse = 0

Lorsque l’on instanciera un nouvel objet **Satellite()**, on pourra choisir son nom, _sa masse_ et _sa vitesse_ .

Les méthodes suivantes seront définies :

* **impulsion(force, duree)** permettra de faire varier la vitesse du satellite. 

Pour savoir comment, rappelez-vous votre cours de physique : 

la variation de vitesse ```Δ v``` subie par un objet de masse **m** soumis à l’action d’une force **F** pendant un temps **t** vaut 

```
v = F × t
     -----
       m
```

Par exemple : un satellite de 300 kg qui subit une force de 600 Newtons pendant 10 secondes
voit sa vitesse augmenter (ou diminuer) de 20 m/s.

* affiche_vitesse() affichera le nom du satellite et sa vitesse courante.
* energie() renverra au programme appelant la valeur de l’énergie cinétique du satellite.
    
    > Rappel : l’énergie cinétique se calcule à l’aide de la formule 
   
    ```
    Ec=m×v2
    -------
       2
    ```

Exemples d’utilisation de cette classe :

```
>>> s1 = Satellite( ' Zoé ' , masse =250, vitesse =10)
>>> s1.impulsion(500, 15)
>>> s1.affiche_vitesse()
vitesse du satellite Zoé = 40 m/s.
>>> print (s1.energie)
200000
>>> s1.impulsion(500, 15)
>>> s1.affiche_vitesse()
vitesse du satellite Zoé = 70 m/s.
>>> print (s1.energie)
612500
```