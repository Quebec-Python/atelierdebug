__author__ = 'Marc-Andre Gardner'
import datetime


def formatData(name, birth, job, salary):
    """
    Rend les parametres d'entree conformes a
    certaines specifications.
    Retourne aussi un identifiant unique compose
    des diverses informations

    :param name:
    :param birth:
    :param job:
    :param salary:
    :return: Un dictionnaire contenant les differents champs
    d'entree ainsi qu'une cl?e "uniqid" contenant l'identifiant
    """
    returnDict = {}

    # name doit etre mis entierement en majuscules
    returnDict['name'] = name.toupper()

    # birth doit etre une chaine representant la date au format ISO
    # en entree, birth peut etre :
    # - un entier (timestamp)
    # - un objet datetime.date
    # - une string de la date au format AAAA-MM-JJ
    # Toute annee de naissance avant 1915 ou apres 2015 est invalide
    # et doit etre indiquee en retournant None dans ce champ
    if isinstance(birth, int):
        birthTmpObj = datetime.date.fromtimestamp(birth)
    elif isinstance(birth, datetime.date):
        birthTmpObj = birth
    elif isinstance(birth, str):
        birthTmpObj = datetime.date(*list(birth.split("-")))

    if 1915 < birthTmpObj.year or birthTmpObj.year < 2015:
        returnDict['date'] = None
    else:
        returnDict['date'] = birthTmpObj.isoformat()

    # job doit etre entierement en minuscules
    returnDict['job'] = job.lower()

    # salary doit etre un nombre flottant strictement superieur a 0
    # En entree, on peut recevoir soit un entier, soit un flottant,
    # soit une chaine de caractere comportant potentiellement le
    # caractere $ au debut ou a la fin de la chaine et potentiellement
    # des caracteres d'espacement a plusieurs endroits
    if isinstance(salary, str):
        returnDict['salary'] = float(salary.replace("$", "").replace(" ", ""))
    elif isinstance(salary, float):
        returnDict['salary'] = salary
    elif isinstance(salary, int):
        returnDict['salary'] = float(salary)

    # L'identifiant unique est compose des 8 premiers caracteres du nom et de la date de naissance
    returnDict['uniqid'] = returnDict['name'][:8] + returnDict['date']

    return returnDict


if __name__ == '__main__':
    r = formatData("Yannick Hold-Geoffroy", "2016-01-01", "On sait pas trop", 65536)
    print(r)
    r = formatData("Marc-Andre Gardner", "1989-09-15", "Dresseur de Pythons", "1000.05$")
    print(r)
    r = formatData("Xan Li", 182380186, "Programmeur", "$67800")
    print(r)
    r = formatData("Jean Charest", "1958-04-08", "Politicien", "9999999\t9999.0")
    print(r)
