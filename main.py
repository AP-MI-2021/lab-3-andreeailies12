def printmenu():
    print("1. Citire lista.")
    print("2. Concatenarea numerelor din subsecvență are cifrele în ordine crescătoare.")
    print("3. Produsul numerelor este impar.")
    print("4. Toate numerele sa fie pare.")
    print("5. Iesire")


def citirelista():
    l = []
    givenString = input("dati lista cu elemente separate prin virgula")
    numberAsString = givenString.split(",")
    for x in numberAsString:
        l.append(int(x))
    return l


def concatenareNumere(l):
    """
    Determina concatenarea numerelor din lista si verificarea daca are cifrele in ordine crescatoare
    :param l: lista de numere
    :return:  True daca numarul concatenat cu cifrele in ordine crescatoare, in caz contrar False
    """
    nr = ""
    for i in range(len(l)):
        nr = nr + str(l[i])

    nr = int(nr)

    while nr > 9:
        a = nr % 10
        b = nr // 10 % 10
        nr //= 10  # nr = nr  // 10
        if a < b:
            return False

    return True


def test_concatenareNumere():
    assert get_longest_concat_digits_asc([2, 56, 8]) == [2, 56, 8]
    assert get_longest_concat_digits_asc([1, 856, 1]) == [1]
    assert get_longest_concat_digits_asc([1, 87, 3]) == [1]


def produsImpar(l):
    """
    Determinare daca produsul numarul e impar
    :param l: lista de numere
    :return: True, daca produsul e impar, False in caz contrar
    """
    nr = 1
    for i in range(len(l)):
        nr = nr * int(l[i])
    if nr % 2 == 1:
        return True
    return False


def test_produsImpar():
    assert get_longest_product_is_odd([2, 3, 1]) == [3, 1]
    assert get_longest_product_is_odd([5, 25, 3]) == [5, 25, 3]
    assert get_longest_product_is_odd([1, 1, 9]) == [1, 1, 9]


def numerelePare(l):
    """
    Determina numerele pare dintr o lista
    :param l: lista de numere
    :return: False daca numerele is impare, in caz contrat True
    """
    for i in range(len(l)):
        if l[i] % 2 == 1:
            return False
    return True


def test_numerelePare():
    assert get_longest_all_even([1, 9, 2, 4, 5]) == [2, 4]
    assert get_longest_all_even([2, 5, 3]) == [2]
    assert get_longest_all_even([8, 2, 12, 14, 15, 4]) == [8, 2, 12, 14]


def get_longest_concat_digits_asc(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga subsecventa unde concatenarea numerelor din lista sa aiba cifrele in ordine crescatoare.
    l = lista numere
    returneaza cea mai lunga subsecventa unde concatenarea numerelor din lista sa aiba cifrele in ordine crescatoare
    """
    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):  # luam de la i ca sa avem si subsec de un singur numar
            if concatenareNumere(lst[i:j + 1]) and len(subsecventamax) < len(lst[i:j + 1]):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def get_longest_product_is_odd(lst: list[int]) -> list[int]:
    """
     Determina cea mai lunga subsecventa unde produsul numerelor sa fie impar
    :param lst: lista de numere
    :return:cea mai lunga subsecventa unde produsul numerelor sa fie impar
    """
    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):  # luam de la i ca sa avem si subsec de un singur numar
            if produsImpar(lst[i:j + 1]) and len(subsecventamax) < len(lst[i:j + 1]):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def get_longest_all_even(lst: list[int]) -> list[int]:
    """
     Determina cea mai lunga subsecventa unde numerele is pare
    :param lst: lista de numere
    :return:cea mai lunga subsecventa unde numerele is pare
    """

    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):  # luam de la i ca sa avem si subsec de un singur numar
            if numerelePare(lst[i:j + 1]) and len(subsecventamax) < len(lst[i:j + 1]):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def main():# incepe meniul
    test_concatenareNumere()
    test_produsImpar()
    test_numerelePare()
    l = []

    while True:
        printmenu()  # apelez functia care imi printeaza meniul
        optiune = input("dati optiune: ")
        if optiune == "1":
            l = citirelista()
        elif optiune =="2":
            print(get_longest_concat_digits_asc(l))
        elif optiune == "3":
            print(get_longest_product_is_odd(l))
        elif optiune == "4":
            print(get_longest_all_even(l))
        elif optiune == "5":
            break  # ne scoate din cea mai apropiata instructiune repetitiva, adica while in cazul nostru
        else:
            print("optiune gresita. reincercati")


if __name__ == '__main__':
    main()