eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


print("Выберите язык: aнгл=e, рус=r")
lan = input()
print("Выберите шифрование: шифрование - ch, дешифрование - def")
chif = input()
print("Введите ключ шифрования")
n = int(input())
print("Введите фразу")
f = input()


def cezar(f, l, c, n):
    """Функция шифрования дешифрования цезаря"""
    rez = ""
    # Режим шифрования
    if c == "ch":
        # выбор английского языка
        if l == "e":
            for i in f:
                if i in eng_lower_alphabet:
                    rez += eng_lower_alphabet[
                        (eng_lower_alphabet.index(i) + n) % len(eng_lower_alphabet)
                    ]
                elif i in eng_upper_alphabet:
                    rez += eng_upper_alphabet[
                        (eng_upper_alphabet.index(i) + n) % len(eng_upper_alphabet)
                    ]
                else:
                    rez += i
        # выбор русского языка
        else:
            for i in f:
                if i in rus_lower_alphabet:
                    rez += rus_lower_alphabet[
                        (rus_lower_alphabet.index(i) + n) % len(rus_lower_alphabet)
                    ]
                elif i in rus_upper_alphabet:
                    rez += rus_upper_alphabet[
                        (rus_upper_alphabet.index(i) + n) % len(rus_upper_alphabet)
                    ]
                else:
                    rez += i

    # Режим дешифрования
    else:
        if l == "e":
            for i in f:
                if i in eng_lower_alphabet:
                    rez += eng_lower_alphabet[
                        (eng_lower_alphabet.index(i) - n) % len(eng_lower_alphabet)
                    ]
                elif i in eng_upper_alphabet:
                    rez += eng_upper_alphabet[
                        (eng_upper_alphabet.index(i) - n) % len(eng_upper_alphabet)
                    ]
                else:
                    rez += i
        # выбор русского языка
        else:
            for i in f:
                if i in rus_lower_alphabet:
                    rez += rus_lower_alphabet[
                        (rus_lower_alphabet.index(i) - n) % len(rus_lower_alphabet)
                    ]
                elif i in rus_upper_alphabet:
                    rez += rus_upper_alphabet[
                        (rus_upper_alphabet.index(i) - n) % len(rus_upper_alphabet)
                    ]
                else:
                    rez += i

    return rez


print(cezar(f, lan, chif, n))
