from random import randint

premio = float(input("Qual será o valor do prêmio em milhões: [Ex: 100 Milhôes] "))
print(f'RODADA VALENDO {premio} MILHÕES DE REIAS!!!')
print()
print("Números sorteados de 1 a 60!")

# Números da loteria
# Lógica para que o random não gere números repetidos

loteria = []
numRepetido = True
pos = 0
soma = 0

while numRepetido == True:
    for i in range(6):
        loteria.append(randint(1,60))

    for pos in range(6):
        for numLista in loteria:
            if loteria[pos] == numLista:
                soma += 1
        if soma == 1:
            soma = 0

    if soma >= 2:
        numRepetido = True
        soma = 0
        loteria = []
    else:
        numRepetido = False

#

rodada = 1
jogadores = []
while True:
    jogada = []
    print(f"Jogador {rodada} fazendo seu Jogo!")
    for jogo in range(6):
        jogada.append(int(input("Digite sua jogada: ")))
    jogadores.append(jogada)

    cont = int(input("Existem mais jogadores? [0 para parar] "))
    print()
    if cont == 0:
        break
    rodada += 1

quadra = []
quina = []
total = []
for i in range(len(jogadores)):
    acertos = 0
    x = 0
    while x != len(jogadores[i]):
        for num in loteria:
            if num == jogadores[i][x]:
                acertos += 1
        else:
            x += 1

    if acertos == 4:
        quadra.append(jogadores[i])

    elif acertos == 5:
        quina.append(jogadores[i])

    elif acertos == 6:
        total.append(jogadores[i])

print(f"Números da loteria foram {loteria}")

if len(quadra) > 0:
    premioQuadra = premio * 0.20 / len(quadra)
    print(f"{len(quadra)} jogador(es) acertaram na quadra e ganharam {premioQuadra} Milhôes de reais cada um.")
    print(f"Com os números {quadra}")

if len(quina) > 0:
    premioQuina = premio * 0.30 / len(quina)
    print(f"{len(quina)} jogador(es) acertaram na quina e ganharam {premioQuina} Milhôes de reais cada um.")
    print(f"Com os números {quina}")

if len(total) > 0:
    premioTotal = premio * 0.50 / len(total)
    print(f"{len(total)} jogador(es) acertaram todos os números e ganharam {premioTotal} Milhôes de reais cada um.")
    print(f"Com os números {total}")

if len(quadra) == 0 and len(quina) == 0 and len(total) == 0:
  print("Ninguem foi premiado!")