# Usando objetos OrderedDict
from collections import OrderedDict


def main():
    # Lista de times com número de partidas perdidadas e ganhas
    times_fut = [("Cruzeiro", (18, 12)), ("Vasco", (24, 6)), 
                 ("Avaí", (20, 10)), ("Flamengo", (22, 8)),
                 ("Palmeiras", (15, 15)), ("Santos", (20, 10)), 
                 ("Botafogo", (16, 14)), ("Fluminense", (25, 5))]

    # Ordenando os times pela quantidade de vitórias
    times_ord = sorted(times_fut, key=lambda t: t[1][0], reverse=True)

    # TODO: Crie um dicionário ordenado com os times
    times = OrderedDict(times_ord)
    print(times)

    # TODO: Use popitem para remover o item do topo #retorno de uma tupla com o nome e estatistica definida
    nome, estatistica = times.popitem(False)
    print("Time mais vitorioso: ", nome, estatistica)

    # TODO: Faça um teste de igualdade
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    # b = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    
    print("teste de igualdade:" , a == b)

if __name__ == "__main__":
    main()
