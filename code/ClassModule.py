class Module():
    def __init__(self):
        pass

class Shield(Module):
    def __init__(self, vaisseau):
        self.nom = "Shield"
        self.effet = vaisseau.shield * 0.20 # 2+0% au bouclier du vaisseau
        self.prix = vaisseau.prix * 1.5 # 150% du prix du vaisseau
        self.compatible = "MicroDelta MiliDelta DecaDelta MegaDelta GigaDelta"
    
    def VerifierCompatibilite(self, vaisseau):
        if vaisseau.modele in self.compatible:
            return True
        else:
            return False

class Visee(Module):
    def __init__(self, vaisseau):
        self.nom = "Visee"
        self.effet = vaisseau.visee * 0.50 # +50% à la précision de la visée du vaisseau
        self.prix = vaisseau.prix * 1.25 # 125% du prix du vaisseau
        self.compatible = "MicroDelta MiliDelta DecaDelta MegaDelta GigaDelta"
    
    def VerifierCompatibilite(self, vaisseau):
        if vaisseau.modele in self.compatible:
            return True
        else:
            return False

class Speed(Module):
    def __init__(self, vaisseau):
        self.nom = "Speed"
        self.effet = vaisseau.speed * 0.50 # +50% du bouclier du vaisseau
        self.prix = vaisseau.prix * 1.5 # 150% du prix du vaisseau
        self.compatible = "DecaDelta MegaDelta GigaDelta"
    
    def VerifierCompatibilite(self, vaisseau):
        if vaisseau.modele in self.compatible:
            return True
        else:
            return False

class Maniabilite(Module):
    def __init__(self, vaisseau):
        self.nom = "Maniabilite"
        self.effet = vaisseau.Maniabilite * 0.15 # +15% à la maniabilité du vaisseau
        self.prix = vaisseau.prix * 1.5 # 150% du prix du vaisseau
        self.compatible = "MicroDelta MiliDelta DecaDelta"
    
    def VerifierCompatibilite(self, vaisseau):
        if vaisseau.modele in self.compatible:
            return True
        else:
            return False

class Portee(Module):
    def __init__(self, vaisseau):
        self.nom = "Portee"
        self.effet = vaisseau.Portee * 0.10 # +10% à la maniabilité du vaisseau
        self.prix = vaisseau.prix * 1.75 # 175% du prix du vaisseau
        self.compatible = "DecaDelta MegaDelta GigaDelta"
    
    def VerifierCompatibilite(self, vaisseau):
        if vaisseau.modele in self.compatible:
            return True
        else:
            return False