import random

prefixos = ["Giga", "Mega", "Mini", "Dark", "Fire", "Thunder"]
sufixos = ["zilla", "tron", "monster", "creep", "fang", "storm" ]

def gerar_nome_monstro():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    nome = prefixo + sufixo
    return nome

print("Bem-vindo ao Gerador de Nome de Monstro!")
print("Seu monstro é:", gerar_nome_monstro())