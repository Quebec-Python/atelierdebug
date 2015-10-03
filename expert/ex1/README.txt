Process qui ne termine jamais

# Pyrasite version
##################

Requis: pip install pyrasite

python ex1.py

#get the PID using / (search)
ps aux | grep ex1.py    (ou htop)

pyrasite <PID> payload.py

# Manhole version
#################

Exécuter:
python ex1_manhole.py

Exemples d'emploi:
netcat -U /tmp/manhole-1234
socat - unix-connect:/tmp/manhole-1234
socat readline unix-connect:/tmp/manhole-1234


# GDB version
#############

Prérequis: Python compilé avec support GDB et les extensions GDB (disponible sur Ubuntu dans le paquet python3-dbg)

Connecter déjà en train d'exécuter:
gdb python3 <pid>

py-list
py-bt
info threads
continue

Voir la position de tous les threads en Python:
thread apply all py-list

