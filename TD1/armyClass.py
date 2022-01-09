from charactersClass import Character


class Army:
    chef = Character("","",0,"",0)
    moraleBase = 0

    def __init__(self,chef,moraleBase):
        self.chef = chef
        self.moraleBase = moraleBase

    # GETTER / SETTER chef
    def get_chef(self):
        return self.chef

    def set_chef(self, chef):
        self.chef = chef

    # GETTER / SETTER moraleBase
    def get_moraleBase(self):
        return self.moraleBase

    def set_moraleBase(self, moraleBase):
        self.moraleBase = moraleBase

    def __repr__(self):
        res = 'Army('+self.chef+','+str(self.moraleBase)+')'
        return res

    def get_total_morale(self):
        total = self.moraleBase * float(self.chef.get_boostMorale())
        return total