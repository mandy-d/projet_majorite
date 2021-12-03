import csv


def fn_question(question):
    return input(question)


def fn_encode(nom, prenom, age):
    file_csv = "formulaire_majorite.csv"
    header = ["nom", "prenom", "age"]
    data = [nom, prenom, age]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)

def fn_age(age):
    if age >= 18:
        print(prenom2, nom2, "est majeur")
    else:
        print(prenom2, nom2, "est mineur")

q_nom = "Entrer votre nom : ""\n"
nom2 = fn_question(q_nom)
q_prenom = "Entrer votre prenom : ""\n"
prenom2 = fn_question(q_prenom)
q_age = "Entrez votre age : ""\n"
age2 = int(fn_question(q_age))
fn_age(age2)
fn_encode(nom2, prenom2, age2)
