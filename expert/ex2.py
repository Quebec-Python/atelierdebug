import math



def deg2rad(angles):
    out = []
    for theta in angles:
        out.append(lambda: theta/180.*math.pi)
    return out



if __name__ == '__main__':
    for radAnglesFunc in deg2rad([180, 90, 0, 150]):
        print(radAnglesFunc())

