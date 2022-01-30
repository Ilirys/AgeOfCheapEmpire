class IADTO:
    def __init__(self, team="red", strategy="vague", pop_vague=1, attaque_valide=0, demande_valide=0, attaque_en_cours=0, evolution=0,number_of_buildings=0,action_faite=0,compteur_construction_bat=0, barrack_x=0, barrack_y=0):
        self.team = team
        self.strategy = strategy
        self.pop_vague = pop_vague
        self.attaque_valide = attaque_valide
        self.demande_valide = demande_valide
        self.attaque_en_cours = attaque_en_cours
        self.evolution = evolution
        self.number_of_buildings = number_of_buildings
        self.action_faite = action_faite
        self.compteur_construction_bat = compteur_construction_bat
        self.barrack_x = barrack_x
        self.barrack_y = barrack_y
