import sys # modul m.in. do pobierania wartosci

# *args <-- oznacza argumenty bez kluczy czyli np funkcja(1,2,3,4)
# **kwargs <-- oznacza argumenty *Z* kluczami czyli np. funkcja(a=1,b=2)

def arguments_args(*args):  # bierze tyle argumentow ile podasz
    print(f'Jestem w funkcji: {arguments_args.__name__}')
    print('Wypisuje wartosci argumentow:')
    for arg in args:
        print(arg)

# zapis *args <-- mozliwosc podania dowolnej liczby parametrow

def arguments_kwargs(*args, **kwargs):
    print(f'Jestem w funkcji: {arguments_kwargs.__name__}')
    print('Wypisuje wartosci argumentow z kluczami:')
    for key in kwargs:
        print(f'For Key: {key}, value {kwargs[key]}')

def main():
        n = len(sys.argv)
        print(f'gotten {n} arguments')
        # arguments_args(sys.argv)
        kwargs = dict(arg.split('=') for arg in sys.argv[1:])
        arguments_kwargs(sys.argv,**kwargs)
        # polecenie python ex_01_args_kwargs.py 2 3 a=2 b=3
        moja_sciezka = kwargs['input_data']

if __name__ == "__main__":
    print('Start!')
    main()

























