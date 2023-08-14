import re

def verifica(senha):
        if re.match(f"\w*[A-Z]\w*", senha) and re.match(f"\w*[a-z]\w*", senha) and re.match(f"[0-9]*", senha):
            return True
        else: return False

while True:
    senha = input()
    if senha == '':
        break
    aux = verifica(senha)
    if ' ' in senha or len(senha) < 6 or len(senha) > 32 or aux == False:
        print('Senha invalida.')
    else:
        print('Senha valida.')
