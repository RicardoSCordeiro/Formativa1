import random

prefixos = ["Giga", "Mega", "Mini", "Dark", "Fire", "Ice", "Thunder"]
sufixos = ["zilla", "tron", "monster", "creep", "fang", "storm", "wolf"]

def gerar_nome_monstro():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    nome = prefixo + sufixo
    return nome

print("Bem-vindo ao Gerador de Nome de Monstro!")
print("Seu monstro é chamado:", gerar_nome_monstro())