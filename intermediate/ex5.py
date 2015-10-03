from collections import namedtuple
from base64 import b64encode

def myFunction(data, reportError=False):
    """
    Retourne la page correspondant à chaque
    entrée du dictionnaire, selon l'âge
    de la personne enregistrée. Si reportError
    est à True, alors soulève une exception de
    type ValueError lorsque l'âge est invalide,
    sinon retourne simplement la page d'index.
    """
    listPages = []
    for k,v in data.items():
        if k == "nobody":
            continue
        else:
            if v.age < 2:
                page = "page0-2.php3"
            elif v.age < 4:
                page = "page2-4.php3"
            elif v.age < 10:
                page = "page4-10.php3"
            elif v.age < 16:
                page = "page10-16.php3"
            elif v.age < 20:
                page = "page16-20.php3"
            elif v.age < 30:
                page = "page20-30.php3"
            elif v.age < 40:
                page = "page30-40.php3"
            elif v.age < 50:
                page = "page40-50.php3"
            elif v.age < 60:
                page = "page50-60.php3"
            elif v.age < 70:
                page = "page60-70.php3"
            elif v.age < 120:
                page = "vieux.php"
            else:
                page = "index.php"
                if reportError:
                    raise ValueError("Valeur d'âge incorrecte!")

                
                if v.profession != "":
                    page += "?emploi={}".format(b64encode(v.profession))
                listPages.append(page)
    return listPages

        

if __name__=="__main__":
    typePerson = namedtuple('Personne', ['age', 'profession'])
    d = {'moi' : typePerson(age=28, profession=""),
            'toi' : typePerson(age=38, profession=""),
            'lui' : typePerson(age=4, profession=""),
            }
    print(myFunction(d))        # Devrait afficher ['page20-30.php3', 'page30-40.php3', 'page2-4.php3']