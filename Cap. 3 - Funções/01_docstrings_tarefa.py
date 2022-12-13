# Usando docstrings para documentar métodos
#Terminal
# >>> print(map.__doc__)
# >>> import collections
# >>> print(collections.__doc__)

#https://www.python.org/dev/peps/pep-257

def minha_funcao(arg1, arg2=None):
    """Minha função executa um print dos argumentos passados
    
    Params:
    arg1: Primeiro argumento
    arg2: Segundo argumento, Default = None
    
    """
    print(arg1, arg2)

def main():
    print(minha_funcao.__doc__)


if __name__ == "__main__":
    main()
