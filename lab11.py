from dataclasses import dataclass

@dataclass
class player:
    def __init__(self, vida, dano, x, y):
        self.vida = vida
        self.dano = dano
        self.x = x
        self.y = y
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, vida):
        self._vida = vida


def main():

    zelda = player()

    linha = input().split()  # vida e dano iniciais
    zelda = int(linha[0])
    dp = int(linha[1])
    linha = input().split()  # tamanho do mapa
    n = int(linha[0])
    m = int(linha[1])
    linha = input().split(",")  # posições iniciais do Link
    xi = int(linha[0])
    yi = int(linha[1])
    linha = input().split(",")  # posições da saída
    xf = int(linha[0])
    yf = int(linha[1])
    q = int(input())  # número de monstros
    monstro = {}
    for i in range(q):
        linha = input().split()  # vida, ataque, tipo e posição
        pos = linha[3].split(",")
        monstro[i] = [int(linha[0]), int(linha[1]), linha[2], int(pos[0]), int(pos[1])]
    b = int(input())  # número de objetos
    objeto = {}
    for i in range(b):
        linha = input().split()  # nome, tipo, posição e status
        pos = linha[2].split(",")
        objeto[i] = [linha[0], linha[1], int(pos[0]), int(pos[1]), int(linha[3])]
    
    mapa = []
    # mapa ainda vazio
    for i in range(n):
        mapa.append([])
        for j in range(m):
            mapa[i].append('.')
    updated = mapa  # Matriz para marcar quais posições foram atualizadas

    # objetos
    for i in objeto:
        mapa[objeto[i][2]][objeto[i][3]] = objeto[i][1]
    # monstros em suas posições iniciais
    for i in monstro:
        mapa[monstro[i][3]][monstro[i][4]] = monstro[i][2]

    mapa[xf][yf] = '*'  # Saída
    mapa[xi][yi] = 'P'  # Posição inicial do Link

    print_mat(mapa)
    # posição atual de Link
    x = xi
    y = yi
    desceu = False  # Se Link já chegou na ultima linha como a maldição o obriga
    while 1:
        if x == n-1:
            desceu = True
        x, y = move_Link(x, y, mapa, n, m, desceu)

        
        # checando se algum objeto foi coletado
        for i in objeto:
            # posição do objeto i
            xo = objeto[i][2]
            yo = objeto[i][3]
            nome = objeto[i][0]
            tipo = objeto[i][1]
            status = objeto[i][2]
            updated[xo][yo] = 1

            if xo == x and yo == y:
                print("[{}]Personagem adquiriu o objeto {} com status de {}".format(tipo, nome, status))
                objeto.pop(i)
                if tipo == 'v':
                    vp += status
                else:
                    dp += status

        combate = []
        # movendo os monstros
        for i in monstro:
            # posição do monstro i
            xm = monstro[i][3]
            ym = monstro[i][4]
            tipo = monstro[i][2]

            if tipo == 'U':
                if xm > 0:
                    xm -= 1
            elif tipo == 'R':
                if ym < m-1:
                    ym += 1
            elif tipo == 'R':
                if xm < m-1:
                    xm += 1
            else:
                if ym > 0:
                    ym -= 1
            
            mapa[xm][ym] = tipo
            monstro[i][3] = xm
            monstro[i][4] = ym
            updated[xm][ym] = 1
            if xm == x and ym == y:
                combate.append(i)  # monstro i vai entrar em combate com Link
        
        if x == xf and y == yf:
            mapa[x][y] = 'P'
            print("Chegou ao fim!")
            break

        # executando combate caso exista algum monstro junto com o Link
        if len(combate) != 0:
            combate
            
        mapa[xf][yf] = '*'  # Saída
        mapa[x][y] = 'P'



def print_mat(matriz):
    """Imprime a matriz recebida."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j < len(matriz[i])-1:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j])


def move_Link(x, y, mapa, n, m, desceu):
    """Muda a posição de Link na matriz para a próxima."""
    if desceu is not True:
        x += 1  # já chequei antes se era a última linha
    else:
        if x%2 == 0:
            if y > 0:
                y -= 1
            else:
                x -= 1
        else:
            if y < m-1:
                y += 1
            else:
                x -= 1
    return x, y


if __name__ == "__main__":
    main()
