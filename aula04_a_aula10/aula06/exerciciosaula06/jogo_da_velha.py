import velhafuncoes as jv

jogador = 'X'

vencendor = False

while vencendor == False:
    jv.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar? \n'))

    jv.jogar(jogada, jogador)

    jv.desenhar_tabuleiro()

    jogador = jv.troca_jogador(jogador)
    vencendor = jv.verifica_vitoria()

jogador = jv.troca_jogador(jogador)
print(f'O JOGADOR "{jogador}" venceu')
