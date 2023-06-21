from math import floor


def main():
    vida = int(input())
    vida_max = vida
    f = input().split()
    flechas = {}
    for i in range(0, len(f), 2):
        flechas[f[i]] = int(f[i+1])
    n = int(input())

    sem_flechas = False
    derrotada = False
    combate = 0
    c = 0  # Variável para saber quando já se passou por todos os monstros
    while c < n:
        flechas_porcombate = flechas.copy()
        acertou_critico = {}
        critico = {}
        # input informações dos monstros
        u = int(input())
        monstro = {}
        partes = {}
        for i in range(u):
            info = input().split()
            monstro[i] = [int(info[0]), int(info[1]), int(info[2])]  # vida, ataque, partes
            partes[i] = {}
            critico[i] = {}
            for j in range(monstro[i][2]):
                p = input().split(", ")
                partes[i][p[0]] = [p[1], int(p[2]), int(p[3]), int(p[4])]  # fraqueza, dano max, posição
                critico[i][p[0]] = [int(p[3]), int(p[4]), 0]  # posição, quantas vezes foi acertado
        c += u

        if derrotada or sem_flechas:
            continue

        ini_vivos = u
        ataque_num = 0  # quantos ataques seguidos Aloy já fez no combate atual
        print("Combate", combate, end=", ")
        print("vida =", vida)
        while ini_vivos > 0:

            ataque = input().split(", ")  # alvo, parte, flecha, posição
            print(ataque)
            if flechas_porcombate[ataque[2]] == 0:
                sem_flechas = True
                break

            flechas_porcombate[ataque[2]] -= 1
            alvo = int(ataque[0])
            dist = abs(int(ataque[3]) - partes[alvo][ataque[1]][2]) + abs(int(ataque[4]) - partes[alvo][ataque[1]][3])
            dano = partes[alvo][ataque[1]][1] - dist  # dano maximo - distancia
            dano = max(dano, 0)
            # se a flecha não é fraqueza:
            if partes[alvo][ataque[1]][0] != "todas" and partes[alvo][ataque[1]][0] != ataque[2]:
                dano //= 2
            if dist == 0:
                acertou_critico[alvo] = True
                critico[alvo][ataque[1]][2] += 1

            ataque_num += 1
            monstro[alvo][0] -= dano
            if monstro[alvo][0] <= 0:
                print("Máquina", ataque[0], "derrotada")
                ini_vivos -= 1

            if ataque_num == 3:
                ataque_num = 0
                for i in range(u):
                    if monstro[i][0] > 0:  # monstro i está vivo
                        vida -= monstro[i][1]  # então ataca
                if vida <= 0:
                    derrotada = True
                    break

        print("Vida após o combate =", max(vida, 0))
        if derrotada or sem_flechas:
            continue
        combate += 1
        print("Flechas utilizadas:")
        for i in flechas:
            if flechas[i]-flechas_porcombate[i] > 0:
                print("- " + i + ": " + str(flechas[i] - flechas_porcombate[i]) + "/" + str(flechas[i]))
        if len(acertou_critico) > 0:
            print("Críticos acertados:")
            for i in critico:
                if i not in acertou_critico:
                    continue
                print("Máquina", i, end=":\n")
                for j in critico[i]:
                    if critico[i][j][2] != 0:
                        print("- (" + str(critico[i][j][0]) + ", " + str(critico[i][j][1]) + "): " + str(critico[i][j][2]) + "x")

        vida = min(vida_max, vida + floor(0.5 * vida_max))

    if sem_flechas:
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
    elif derrotada:
        print("Aloy foi derrotada em combate e não retornará a tribo.")
    else:
        print("Aloy provou seu valor e voltou para sua tribo.")


if __name__ == "__main__":
    main()
