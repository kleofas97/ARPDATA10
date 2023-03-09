"""
    Napisz funkcje laczaca ze soba dwa napisy w sposob:
    najpierw pierwsza litera pierwszego napisu, potem pierwsza litera
    drugiego, druga litera drugiego napisu, itd...
    Funkcja powinna zwrocic nowy napis bedacy polaczeniem tych podanych
    jako parametry. Uwaga: wejsciowe napisy nie musza byc tej samej
    dlugosci!
    Przyklad:
    >> merge_strings("pies", "buda")
    pbiuedsa
    >> merge_strings("stop", "supermarket)
    sstuoopermarket
    W przypadku kiedy jakis napis jest dluzszy, nalezy go po prostu
    przepisac, podobnie jak to zostalo pokazane na drugim przykladzie.
"""

import time


def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()

        result = func(*args, **kwargs)

        t2 = time.time()

        print(f"Function {func.__name__} executed in {(t2 - t1):.4f}")
        return result

    return wrap_func


@timer
def merge_strings_chatgpt(string1, string2):
    """Laczy naprzemiennie napisy string1 oraz string2.

    :param string1: pierwszy napis do polaczenia.
    :param string2: drugi napis do polaczenia.
    :return: napis zlozony z podanych jako argumenty.

    """
    result = ""
    len1 = len(string1)
    len2 = len(string2)
    max_len = max(len1, len2)
    for i in range(max_len):
        if i < len1:
            result += string1[i]
        if i < len2:
            result += string2[i]
    return result


@timer
def merge_strings_adam(string1, string2):
    end = ""
    new = ""
    length = len(string1)
    if len(string1) > len(string2):
        end = string1[len(string2) :]
        length = len(string2)
    elif len(string2) > len(string1):
        end = string2[len(string1) :]

    for i in range(length):
        new += string1[i] + string2[i]

    return new + end


@timer
def merge_strings_Maurycy(string1, string2):
    string = ""
    for s1, s2 in zip(string1, string2):
        string += s1
        string += s2
    if len(string1) != len(string2):
        if len(string1) < len(string2):
            string += string2[len(string1) :]
        else:
            string += string1[len(string2) :]
    return string


tekst = "tekst" * 100000
teskt2 = "tekst" * 10000000
merge_strings_Maurycy(tekst, teskt2)
merge_strings_adam(tekst, teskt2)
merge_strings_chatgpt(tekst, teskt2)
