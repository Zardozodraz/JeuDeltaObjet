import math

class Vaisseau():
    def __init__(self, id, modele):
        self.id = id
        self.modele = modele
    
    def droite(self, x, y):
        self.position = (x + self.speed, y)
    
    def gauche(self, x, y):
        self.position = (x - self.speed, y)
    
    def haut(self, x, y):
        self.position = (x, y + self.speed)
    
    def bas(self, x, y):
        self.position = (x, y - self.speed)
    
    def tir(self, arme):
        if arme == "missile" and self.missile > 0:
            self.missile -= 1
        elif arme == "advencedMissile" and self.advencedMissile > 0:
            self.advencedMissile -= 1
        else:
            raise ValueError("Arme inconnue")
    
    def cibler(self, positionCible):
        # Calcul de l'angle à avoir pour se diriger vers la cible
        # Vecteur AB
        dx = positionCible[0] - self.position[0] # xB - xA
        dy = positionCible[1] - self.position[1] # yB - yA
        
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        
        # Normaliser l'angle entre 0 et 360
        if angle_deg < 0:
            angle_deg += 360
        
        self.angle = angle_deg

####################################################################################

class MicroDelta(Vaisseau):
    def __init__(self, id, position):
        self.id = id
        self.modele = "MicroDelta"
        self.prix = 500
        
        self.vie = 30
        self.shield = 100
        self.speed = 100
        self.Maniabilite = 1_000
        self.visee = 1_000
        self.portee = 30

        self.canon = 3
        self.ion = 0
        self.missile = 4
        self.advencedMissile = 0
        
        self.position = position # (x, y)
        self.angle = 0
        
        modifier = ""

class MiliDelta(Vaisseau):
    def __init__(self, id, position):
        self.id = id
        self.modele = "MiliDelta"
        self.prix = 1_000
        
        self.vie = 70
        self.shield = 100
        self.Maniabilite = 900
        self.speed = 80
        self.visee = 1_000
        self.portee = 50

        self.canon = 5
        self.ion = 0
        self.missile = 8
        self.advencedMissile = 0
        
        self.position = position # (x, y)
        self.angle = 0
        
        modifier = ""
        
class DecaDelta(Vaisseau):
    def __init__(self, id, position):
        self.id = id
        self.modele = "DecaDelta"
        self.prix = 2_500
        
        self.vie = 150
        self.shield = 100
        self.Maniabilite = 800
        self.speed = 70
        self.visee = 1_000
        self.portee = 100

        self.canon = 10
        self.ion = 2
        self.missile = 20
        self.advencedMissile = 4
        
        self.position = position # (x, y)
        self.angle = 0
        
        modifier = ""

class MegaDelta(Vaisseau):
    def __init__(self, id, position):
        self.id = id
        self.modele = "MegaDelta"
        self.prix = 5_000
        
        self.vie = 300
        self.shield = 100
        self.Maniabilite = 700
        self.speed = 60
        self.visee = 1_000
        self.portee = 150
        
        self.canon = 20
        self.ion = 5
        self.missile = 40
        self.advencedMissile = 10
        
        self.position = position # (x, y)
        self.angle = 0
        
        modifier = ""
    
class GigaDelta(Vaisseau):
    def __init__(self, id, position):
        self.id = id
        self.modele = "GigaDelta"
        self.prix = 10_000
        
        self.vie = 500
        self.shield = 100
        self.Maniabilite = 600
        self.speed = 40
        self.visee = 1_000
        self.portee = 200
        
        self.canon = 35
        self.ion = 10
        self.missile = 75
        self.advencedMissile = 20
        
        self.position = position # (x, y)
        self.angle = 0
        
        modifier = ""