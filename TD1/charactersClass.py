class Character:

    nom = ""
    prenom = ""
    age = 0
    profession = ""
    boostMorale = 0

    def __init__(self, nom, prenom, age, profession, boostMorale):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boostMorale = boostMorale

    # GETTER / SETTER nom
    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    # GETTER / SETTER prenom
    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    # GETTER / SETTER age
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # GETTER / SETTER profession
    def get_profession(self):
        return self.profession

    def set_profession(self, profession):
        self.profession = profession

    # GETTER / SETTER boostMorale
    def get_boostMorale(self):
        return self.boostMorale

    def set_boostMorale(self, boostMorale):
        self.boostMorale = boostMorale

    def __repr__(self):
        res = 'Character('+self.nom+','+self.prenom+','+str(self.age)+','+self.profession+','+str(self.boostMorale)+')'
        return res