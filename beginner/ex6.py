import hashlib
from enum import Enum
from functools import partial

class AccessLevel(Enum):
    """ Access levels definition"""
    NOACCESS = 0
    ADMIN = 1
    USER = 2
    GUEST = 3

def checkValidity(username, password, requireAdmin, userList, adminList, passwordList):
    """
    Vérifie si l'utilisateur 'username' est autorisé et son niveau d'autorisation,
    ainsi que la validité de son mot de passe.
    Retourne le niveau d'autorisation obtenu.
    """
    hashedPassword = hashlib.sha1(password.encode('utf-8')).hexdigest()
    if (username in adminList and requireAdmin) or (username in userList and not requireAdmin) and passwordList[username] == hashedPassword:
        if requireAdmin:
            return AccessLevel.ADMIN
        else:
            return AccessLevel.USER
    else:
        return AccessLevel.NOACCESS


if __name__ == '__main__':
    userList = ["mag", "yan", "david"]
    adminList = ["marc", "christian", "jean-francois"]
    clearPasswords = {"mag" : 'boum', 
                      "yan" : 'paf',
                      "david" : 'bim',
                      "marc" : 'bam!',
                      "christian" : "slam",
                      "jean-francois" : "mumumu"}
    
    hashs = {u:hashlib.sha1(p.encode('utf-8')).hexdigest() for u,p in clearPasswords.items()}
    checkFunc = partial(checkValidity, userList=userList, adminList=adminList, passwordList=hashs)
    
    print("L'utilisateur {} demande un accès utilisateur avec le mot de passe {} : {}".format("mag", "boum", checkFunc("mag", "boum", requireAdmin=False)))         # Devrait être autorisé comme USER
    print("L'utilisateur {} demande un accès administrateur avec le mot de passe {} : {}".format("mag", "boum", checkFunc("mag", "boum", requireAdmin=True)))       # Devrait être refusé comme ADMIN
    print("L'utilisateur {} demande un accès administrateur avec le mot de passe {} : {}".format("christian", "slam", checkFunc("christian", "slam", requireAdmin=True)))   # Devrait être autorisé comme ADMIN
    print("L'utilisateur {} demande un accès utilisateur avec le mot de passe {} : {}".format("yan", "pasbon", checkFunc("yan", "pasbon", requireAdmin=False)))             # Devrait être refusé comme USER
    print("L'utilisateur {} demande un accès administrateur avec le mot de passe {} : {}".format("marc", "choubidouwa", checkFunc("marc", "choubidouwa", requireAdmin=True)))   # Devrait être refusé comme ADMIN
