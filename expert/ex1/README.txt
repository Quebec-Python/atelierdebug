Process hang

# Pyrasite version

python ex1.py

#get the PID using / (search)
ps aux | grep ex1.py    (ou htop)

pyrasite <PID> payload.py


# GDB version

Connecter déjà en train d'exécuter:
gdb python3 <pid>

info threads (?)
py-list
py-bt
pystack

Voir l'état de tous les threads:
thread apply all py-list
