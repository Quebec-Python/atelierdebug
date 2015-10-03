import time

# Exemple qui ne termine jamais
# Voir README.txt


def myFunc(a):
    while True:
        time.sleep(0.5)
        if a < 16:
            break


if __name__ == '__main__':
    for i in range(20):
        myFunc(i)
