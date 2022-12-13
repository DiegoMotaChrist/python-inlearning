# Iteradores do módulo itertools
import itertools


def condicao(x: int):
    return x < 40


def main():
    # TODO: Iterador cycle pode ser usado como o iter para iterar sobre
    # uma lista
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas) #circular - infinito
    print(next(ciclo)) #indice0
    print(next(ciclo)) #indice1
    print(next(ciclo)) #indice2
    print(next(ciclo)) #recomeço

    # TODO: Use count para criar um contador
    contador = itertools.count(100, 10) # a partir do 100 - infinito
    print(next(contador)) #indice0
    print(next(contador)) #indice1
    print(next(contador)) #indice2
    print(next(contador)) #recomeco

    # TODO: A função accumulate cria um iterdor que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores)
    acumuladoMax = itertools.accumulate(valores, max)
    print(list(acumulado))
    print(list(acumuladoMax))

    # TODO: Use a função chain para conectar listas
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    # TODO: As funções dropwhile e takewhile vai retornar valores até
    # que uma condição seja atingida
    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))

if __name__ == "__main__":
    main()
