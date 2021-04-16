import json 


def inscprition():
    dico = {"nom":"","email":"","password":""}
    
    with open('database.json','r') as f:
        liste = json.load(f)
        liste.append(dico)
    
    nom = input('Nom :')
    email = input('Email :')
    password = str(input('Password :'))

    dico["nom"]= nom
    dico["password"] = password

    for mail in liste:
        if email == mail["email"]:
            print("existe")
        else:
            



    with open('database.json','w') as f:
            json.dump(liste,f)
            
            

            
        
    
    



def connexion():
    with open('database.json','r') as f:
        liste = json.load(f)
    # print(s)

    email = input('Email :')
    password = str(input('Password :'))

    if email and password in s:
        print('Bienvenu vous etre connecté')
    else:
        print("veuillez vous inscrit")
        menu()
            

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

