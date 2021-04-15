import json 

liste = []
def inscprition():
    nom = input('Nom :')
    email = input('Email :')
    password = input('Password :')
    liste.append(nom)
    liste.append(password)
    

    
def connexion():
    print('connexion')

def menu():
    print("1: inscription - 2: connexion")
    try:
        choix = input('choix : ')
        choix = int(choix)
        if choix == 1 :
            inscprition()
        elif choix == 2:
            connexion()
    except:
        print(" Veuillez Entrez 1 pour inscription ou 2 pour vous connecté ")

menu()
with open('database.json' ,'w') as f :
    s= json.dump(liste,f)

if email in s:
        print('ce mail existe')
else:
    liste.append(email) 
