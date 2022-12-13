# Usando funções iteradoras como enumerate, zip, iter, next

def main():
    # Defina a lista de dias da semana em Português e English
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # TODO: Use a função iter para criar um iterador sobre uma lista
    iterador_dias = iter(dias)
    print(next(iterador_dias)) #indice0
    print(next(iterador_dias)) #indice1
    print(next(iterador_dias)) #indice2

    # TODO: Use uma função para iterar sobre um arquivo de forma lazy (como realmente preciso)
    with open('Cap. 2 - Funções embutidas/dados.txt', 'r') as fp: #r: leitura, fp: ponteiro atual
        for linha in iter(fp.readline, ''): # '': final do arquivo
            print(linha)

    # TODO: Use a iteração tradicional (range) sobre a lista dias
    for idx in range(len(dias)):
        print(idx, dias[idx])

    # TODO: Usar a função enumerate reduz a quantidade de código e te
    # dá um contador
    for i, dia in enumerate(dias):
        print(i, dia)

    # TODO: Use a função zip para combinar as listas
    for d in zip(dias, dias_en):
        print(d)

    # TODO: Combine zip com enumerate para formatar o resultado
    for idx, dia in enumerate(zip(dias, dias_en)):
        print(idx, dia[0], "=", dia[1], "em Ingles")

if __name__ == "__main__":
    main()
