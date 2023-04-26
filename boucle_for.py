# pour l'index i dans les valeur de 0 à 5 fait
#0 inclu or que 5 est exclu
for i in range(0 ,5):
    print(i)
# faire avec notre code 
nom=""

def afficher_information_personne(nom ,age):
    # afficher le resultat 
    print( "vous vous appelez "+nom +", vous avez " + str(age)+ " ans .")
    #print("l'an prochain  vous aurez "+ str(age+1)+" ans")
    print(f"l'an prochain  vous aurez {str(age+1)}  ans formater")
def demander_age(nom):
    age=0
    while age== 0 :
        age_str=input ("quel est votre age ?")
            # input retoune tjr une chaine de carctére
        try:
            age=int(age_str) 
            # on converti le resultat en entier avec int()
        except:
            # gestion d'une exception
            print("erreur !! vous devez rentrer un nombre pour l'age")
    return age

# demander le nom
def demander_nom():
    reponse_nom=""
    while reponse_nom== "":
        reponse_nom= input("quel est votre nom ?")
    return reponse_nom

#on va utiliser une fonction et on va l'appeler par la suite 
for i in range(0,3):
    
    nom =demander_nom()+" vous etes le personne "+ str(i+1)
    age= demander_age(nom)
    afficher_information_personne(nom,age)   