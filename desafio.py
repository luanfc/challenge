sus = [
    'Charles B. Abbage',
    'Donald Duck Knuth',
    'Ada L. Ovelace',
    'Alan T. Uring',
    'Ivar J. Acobson',
    'Ras Mus Ler Dorf',
]

arm = [
    'Peixeira',
    'DynaTAC 8000X',
    'Trezoitão',
    'Trebuchet',
    'Maça',
    'Gládio',
]

loc = [
    'Redmond',
    'Palo Alto',
    'San Francisco',
    'Tokio',
    'Restaurante no Fim do Universo',
    'São Paulo',
    'Cupertino',
    'Helsinki',
    'Maida Vale',
    'Toronto',
]

# Informa o índice do suspeito, arma e local
correto = [sus[0], arm[0], loc[0]]
indices = [sus.index(correto[0]), arm.index(correto[1]), loc.index(correto[2])]


def solucao(args):

    if sus[args[0] - 1] != correto[0] \
            or arm[args[1] - 1] != correto[1] \
            or loc[args[2] - 1] != correto[2]:
        return 1
    else:
        return 0


def resolvendo():
    cont = 0
    args = []
    while cont >= 0:

        args.append(int(input("Digite o número do suspeito: ")))
        args.append(int(input("Digite o número da arma: ")))
        args.append(int(input("Digite o número do local: ")))

        if solucao(args) == 0:
            print(solucao(args))
            break
        else:
            print(solucao(args))
            cont += 1
            args = []


if __name__ == '__main__':
    resolvendo()
