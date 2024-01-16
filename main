from arquivo import *

while True: 

    pc = escolhaIa()
    print("_"*60)
    print("""
        Pedra Papel ou Tesoura

        Fechar
    """)
    print("_"*60)
    escolha = input('digite:\n').lower()
    if escolha not in ['pedra', 'papel', 'tesoura', 'fechar']:
        print("_"*60)
        print('escolha não identificada.')
    elif escolha == 'fechar':
        print("_"*60)
        print('Até a próxima!')
        break
    else:
        print("_"*60)
        print(joguinho(escolha, pc))
