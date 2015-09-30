

def create_multipliers():
    return [lambda x : i * x for i in range(5)]


if __name__ == '__main__':
    for multiplier in create_multipliers():
        print(multiplier(2)) # Devrait afficher 0, 2, 4, 6, 8
