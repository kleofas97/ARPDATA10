# napisz funkcje ktora njapierw sprawdzi czy input jest stringiem
# a potem zwroci co druga litere, zaczynajac od 2 litery


def odd_indexes(tekst):
    if isinstance(tekst, str):
        return tekst[1::2]
    return None
