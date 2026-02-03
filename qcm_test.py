def lire_fichier():
    res = []
    with open('projet-question.txt','r', encoding="utf8") as f: 
        fichier2 = f.readlines()
        for ligne in fichier2 : 
            ligne = ligne.strip("\n")
            res.append(ligne)
    return res


def separe(tab):
    questions = []
    for question in tab:
        question = question.split(";;")
        questions.append(question)
        
    return questions

def poser_questions(liste):
    tot = 0
    for question in liste :
        print(question[0])
        rep = "Blanc"
        if rep == question[1]:
            print("bravo !")
            tot = tot + 1
        else:
            print("dommage")
    print(tot)

