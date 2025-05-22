import random
import ClassModule

class Missile():
    def __init__(self):
        self.degats = 0
        self.precision = 0
        self.portee = 0
        self.prix = 0
        self.multiplicateurShield = 0
    
    def mofifier(self, vaisseau):
        # Cette fonction permet de modifier les caractéristiques du missile en fonction des modules du vaisseau.
        if vaisseau.modifier == "Visee":
                    self.precision *= ClassModule.Visee.effet

    def shoot(self, vaisseau, vaisseauCible):
        """
        Cette fonction permet de tirer un missile.
        Elle renvoie True si le tir est réussi, False sinon.
        Elle modifie la vie/bouclier du vaisseau cible si le tir est réussi.
        Elle modifie le nombre de missiles du vaisseau tireur.
        """
        if vaisseau.missile > 0:
            # Est-ce que la cible est dans la portée du missile ?
            if vaisseauCible.portee <= self.portee:
                # Est-ce que le tir touche la cible ?
                if random.randint(0, 100) <= self.precision * (1 + vaisseau.visee / 1_000):
                    # Le tir touche la cible
                    vaisseauCible.vie -= self.degats
                    vaisseau.missile -= 1
                    
                    if vaisseauCible.shield > 0:
                        vaisseauCible.shield -= self.degats * self.multiplicateurShield
                        
                    elif vaisseauCible.shield <= 0:
                        vaisseauCible.vie -= self.degats
                                            
                    return True
                
                else:
                    # Le tir rate la cible
                    vaisseau.missile -= 1
                    return False
            else:
                # La cible est hors de portée
                return False

class MissileBasique(Missile):
    def __init__(self):
        self.degats = 20
        self.precision = 75 # 75%
        self.portee = 5
        self.prix = 300
        self.multiplicateurShield = 0.7 # -30% de degats sur le bouclier

class MissileAvance(Missile):
    def __init__(self):
        self.degats = 30
        self.precision = 90 # 90%
        self.portee = 7
        self.prix = 400
        self.multiplicateurShield = 0.9 # -10% de degats sur le bouclier