def main() -> None:
    v = input()
    v = v.split(",")  # vetor inicial

    while 1:
        comando = input()
        if comando == "soma_vetores":
            v2 = input().split(",")
            v = soma_vetores(v, v2)
        elif comando == "subtrai_vetores":
            v2 = input().split(",")
            v = subtrai_vetores(v, v2)
        elif comando == "multiplica_vetores":
            v2 = input().split(",")
            v = multiplica_vetores(v, v2)
        elif comando == "divide_vetores":
            v2 = input().split(",")
            v = divide_vetores(v, v2)
        elif comando == "multiplicacao_escalar":
            e = int(input())
            v = multiplicacao_escalar(v, e)
        elif comando == "n_duplicacao":
            n = int(input())
            v = n_duplicacao(v, n)
        elif comando == "soma_elementos":
            v = soma_elementos(v)
        elif comando == "produto_interno":
            v2 = input().split(",")
            v = produto_interno(v, v2)
        elif comando == "multiplica_todos":
            v2 = input().split(",")
            v = multiplica_todos(v, v2)
        elif comando == "correlacao_cruzada":
            m = input().split(",")
            v = correlacao_cruzada(v, m)
        else:  # fim
            break

        print(v)


def soma_vetores(v1: list, v2: list) -> list:
    tam = max(len(v1), len(v2))
    result = []
    for i in range(tam):
        if len(v1)-1 < i:
            v1.append(0)
        elif len(v2)-1 < i:
            v2.append(0)
        result.append(int(v1[i]) + int(v2[i]))

    return result


def subtrai_vetores(v1: list, v2: list) -> list:
    tam = max(len(v1), len(v2))
    result = []
    for i in range(tam):
        if len(v1)-1 < i:
            v1.append(0)
        elif len(v2)-1 < i:
            v2.append(0)
        result.append(int(v1[i]) - int(v2[i]))

    return result


def multiplica_vetores(v1: list, v2: list) -> list:
    tam = max(len(v1), len(v2))
    result = []
    for i in range(tam):
        if len(v1)-1 < i:
            v1.append(1)
        elif len(v2)-1 < i:
            v2.append(1)
        result.append(int(v1[i]) * int(v2[i]))

    return result


def divide_vetores(v1: list, v2: list) -> list:
    tam = max(len(v1), len(v2))
    result = []
    for i in range(tam):
        if len(v1)-1 < i:
            v1.append(0)
        elif len(v2)-1 < i:
            v2.append(1)
        result.append(int(v1[i]) // int(v2[i]))

    return result


def multiplicacao_escalar(v1: list, e: int) -> list:
    result = []
    for i in range(len(v1)):
        result.append(int(v1[i]) * int(e))

    return result


def n_duplicacao(v1: list, n: int) -> list:
    result = []
    for i in range(n):
        for j in range(len(v1)):
            result.append(int(v1[j]))

    return result


def soma_elementos(v1: list) -> list:
    result = []
    soma = 0
    for i in range(len(v1)):
        soma += int(v1[i])

    result.append(soma)
    return result


def produto_interno(v1: list, v2: list) -> list:
    v = multiplica_vetores(v1, v2)
    v = soma_elementos(v)

    return v


def multiplica_todos(v1: list, v2: list) -> list:
    result = []
    sum = soma_elementos(v2)
    sum = int(sum[0])
    for i in range(len(v1)):
        result.append(sum * int(v1[i]))

    return result


def correlacao_cruzada(v1: list, m: list) -> list:
    result = []
    n = len(v1)
    k = len(m)
    for i in range(n-k+1):
        soma = 0
        for j in range(k):
            soma += int(v1[i+j]) * int(m[j])
        result.append(soma)

    return result


main()
