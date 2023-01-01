import random
import os




opcoes = ['Pedra', 'Papel', 'Tesoura']

pontos_player = 0
pontos_computer = 0
rodada = 6
print('='*40)
print( '\033[1;34;40m ==== Seja Bem-Vindo====\n \t\t=== ao === \n\t  ==== Jogo ====\n == Pedra_Papel_Tesoura == \n\033[m')
print('='*40)

while True:

    for i in range(len(opcoes)):
        print(f'[{i}] {opcoes[i]}')
    print('[3] Sair do Jogo')
    print('*' * 40)
    print()
    print(f'Rodada:{rodada}')
    print('*' * 40)

    if rodada < 1:
        if pontos_player > pontos_computer:
            print('\n\t\t\033[1;32;40m!!!PARABÊNS!!!\033[m\n \033[1;32;40mVOCÊ FOI O GRANDE VENCEDOR!\033[m')
            print(f'\t\t\t\033[1;36;40mPLACAR\033[m \n\t \033[1;34;40mPlayer\033[m {pontos_player} X {pontos_computer} \033[1;37;40mMáquina\033[m\n')
            print('*' * 40)



        elif pontos_player == pontos_computer:
            print('\n\t\t\033[1;35;40mDEU EMPATEEEEEE...!\033[m\n')
            print(f'\t\t\033[1;36;40mPLACAR\033[m \n \033[1;34;40mPlayer\033[m {pontos_player} X {pontos_computer} \033[1;37;40mMáquina\033[m\n')
            print('*' * 40)



        else:
            print('\n\033[1;31;40mINFELISMENTE VOCÊ PERDEU :(\033[m\n')
            print(f'\t\t\033[1;36;40mPLACAR\033[m \n \033[1;34;40mPlayer\033[m {pontos_player} X {pontos_computer} \033[1;37;40mMáquina\033[m\n')
            print('*' * 40)

        break








    player = int(input('Digite uma das opões:'))
    print('=' * 40)
    os.system('clear') or None

    # Gera um número aleatório para a Máquina.
    player_computer = random.randint(0,2)


    if player == 3:
        break

    if  player < 0 or player > 2: # Verifica se a opção escolhida se é válida ou não.
        print('\n!!Opção inválida!!\n')
    else:

        # Verifica a escolha e decide quem ganhou ou perdeu.
        if player == 0:  # Pedra
            if player_computer == 1:
                print('\n\t\t\tVocê perdeu :(\n')
                pontos_computer += 1

            elif player == player_computer:
                print('\n\t\t\tEmpate!\n')
            else:
                print('\n\t\t\tVocê ganhou :)\n')
                pontos_player += 1

        elif player == 1:  # Papel
            if player_computer == 2:
                print('\n\t\t\tVocê perdeu :(\n')
                pontos_computer += 1
            elif player == player_computer:
                print('\n\t\t\tEmpate!\n')
            else:
                print('\n\t\t\tVocê ganhou! :)\n')
                pontos_player += 1
        elif player == 2:# Tesoura
            if player_computer == 0:
                print('\n \t\t\tVocê perdeu :(\n')
                pontos_computer += 1
            elif player == player_computer:
                print('\n\t\t\tEmpate!\n')
            else:
                print('\n\t\t\tVocê ganhou :)\n')
                pontos_player=pontos_player + 1


        rodada-=1

        print('*'*40)

        print(f'Você: {opcoes[player] } \nMáquina: {opcoes[player_computer]}\n')
        print('*' * 40)
        print(f'\t\tPLACAR \n Player {pontos_player} X {pontos_computer} Máquina\n')
        print('*' * 40)