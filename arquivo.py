import random

def escolhaIa():
    return random.choice(['pedra', 'papel', 'tesoura'])
    
def joguinho(usuario, pc):
    if usuario == pc:
        return f'Empate! {usuario} X {pc}'
    elif usuario == 'pedra' and pc == "tesoura":
        return f'Você venceu! {usuario} X {pc}'
    elif usuario == 'papel' and pc == 'pedra':
        return f'Você venceu! {usuario} X {pc}'
    elif usuario == 'tesoura' and pc == 'papel':
        return f'Você venceu! {usuario} X {pc}'
    else:
        return f'Você perdeu! {usuario} X {pc}'
