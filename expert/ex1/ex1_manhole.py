import time
import manhole



def myFunc(a):
    manhole.install(locals={'a': a}, strict=False)
    while True:
        time.sleep(0.5)
        if a < 5:
            break


if __name__ == '__main__':
    for i in range(20):
        myFunc(i)
