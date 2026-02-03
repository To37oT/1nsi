def lire_fichier():
    tab = []
    with open('projet-question.txt','r', encoding="utf8") as f: 
        fichier = f.readlines()
        for ligne in fichier : #regarde chaque ligne
            ligne = ligne.strip("\n") # Supprime les retours à la ligne
            tab.append(ligne) # Ajoute dans un tableau
    return tab #retourner le résultat final


def separe(tableau_question):
    questions_separe = []
    for question in tableau_question: # On regarde chaque élément du tableau questions
        question = question.split(";;") # Coupe chaque question sur les 
        questions_separe.append(question) #Ajouter le résultat dans questions_separe
        
    return questions_separe # retourner le résultat final

def questions(liste_question):
    score = 0
    for question in liste_question :
        print(question[0])
        reponse = "Blanc" # simuler la réponse de l'utilisateur
        if reponse == question[1]:
            print("bravo !")
            score = score + 1
        else:
            print("dommage")
    return score