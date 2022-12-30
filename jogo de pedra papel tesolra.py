import random

# Define as opções de jogo
options = ['pedra', 'papel', 'tesoura']

# Exibe as opções de jogo
print('Opções:')
for i, option in enumerate(options):
    print(f'{i + 1}: {option}')

# Pede para o jogador escolher uma opção
player_choice = int(input('Escolha uma opção: ')) - 1

# Sorteia uma opção para o computador
computer_choice = random.randint(0, 2)

# Exibe as escolhas dos jogadores
print(f'Jogador escolheu {options[player_choice]}')
print(f'Computador escolheu {options[computer_choice]}')

# Verifica o resultado
if player_choice == computer_choice:
    print('Empate!')
elif player_choice == 0 and computer_choice == 2:
    print('Jogador venceu!')
elif player_choice == 1 and computer_choice == 0:
    print('Jogador venceu!')
elif player_choice == 2 and computer_choice == 1:
    print('Jogador venceu!')
else:
    print('Computador venceu!')
