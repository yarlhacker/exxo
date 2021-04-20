import logging
import os
import json

from constante import DATA_DIR

LOGGER = logging.getLogger()

class Listes(list) : 
    def __init__(self,nom,):
        self.nom = nom

    def ajouter(self,element):
        if not isinstance(element,str):
            raise ValueError("Vous ne pouvez qu'ajouter que des chaines caractère ! ")

        if element in self:
            LOGGER.error(f"{element} est déja dans la liste des {self.nom}")
            return False
        
        self.append(element)
        return True
        
    def enlever(self,element):
        if element in self:
            self.remove(element)
            return True
        
        LOGGER.error(f"{element} n'est pas dans  la liste des {self.nom}")
        return False
    
    def afficher(self):
        print(f"Ma Listes des {self.nom}")
        for element in self:
            print(f'- {element}')
    def sauvagarde(self):
        chemin =  os.path.join(DATA_DIR,f'{self.nom}.json')
        if not os.path.exists(DATA_DIR) :
            os.makedirs(DATA_DIR)

        with open(chemin,'w') as f:
            json.dump(self,f, indent=4)
        
        return True

n = input('nom de la liste de courses \ : ')
l = Listes(n)
print(l.nom)
