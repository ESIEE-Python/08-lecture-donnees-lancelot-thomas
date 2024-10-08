"""Permet de traiter les données d'un fichier en parametre"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    lines_file = []
    with open(filename, "r", encoding="utf-8") as f:
        lines_file = f.readlines()
    for line in lines_file:
        list_digit = [int(entier) for entier in line.strip().split(";")]
        l.append(list_digit)
    return l

def get_list_k(data, k):
    """
    renvoie la ligne demandé en parametre
    """
    l = data[k]
    return l

def get_first(l):
    """
    renvoie la première valeur de la liste
    """
    return l[0]

def get_last(l):
    """
    renvoie la derniere valeur de la liste
    """
    return l[-1]

def get_max(l):
    """
    renvoie la valeur max de la liste
    """
    return max(l)

def get_min(l):
    """
    renvoie la valeur min de la liste
    """
    return min(l)

def get_sum(l):
    """
    renvoie la somme de la liste
    """
    return sum(l)

#### Fonction principale


def main():
    """
    main appelant les fonctions secondaire
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
        print(get_first(l), get_last(l), get_max(l), get_min(l), get_sum(l))
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
