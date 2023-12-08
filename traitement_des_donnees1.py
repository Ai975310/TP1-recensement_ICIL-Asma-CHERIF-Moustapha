import csv
import matplotlib.pyplot as plt

# Le Chargement des données
communes_2008 = []
with open("donnees_2008.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        communes_2008.append(row)

communes_2016 = []
with open("donnees_2016.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        communes_2016.append(row)

communes_2021 = []
with open('donnees_2021.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes_2021.append(row)

# Calcul de la somme de population pour chaque année
somme_pop_2008 = sum(int(commune[9]) for commune in communes_2008 if commune[2] == "89")
somme_pop_2016 = sum(int(commune[9]) for commune in communes_2016 if commune[2] == "89")
somme_pop_2021 = sum(int(commune[5]) for commune in communes_2021 if commune[1] == "89")

# Affichage des résultats
print("Somme de la population en 2008 :", somme_pop_2008)
print("Somme de la population en 2016 :", somme_pop_2016)
print("Somme de la population en 2021 :", somme_pop_2021)

# Création d'une courbe
annees = ['2008', '2016', '2021']
populations = [somme_pop_2008, somme_pop_2016, somme_pop_2021]

plt.plot(annees, populations, marker='o')
plt.title('Evolution de la population en 89')
plt.xlabel('Année')
plt.ylabel('Population')
plt.grid(True)
plt.show()
