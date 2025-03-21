import random

prefixos = ["Giga", "Mega", "Mini", "Dark", "Fire", "Ice", "Thunder"]
sufixos = ["zilla", "tron", "monster", "creep", "fang", "storm", "wolf"]

def gerar_nome_monstro():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    nome = prefixo + sufixo
    return nome

print("Bem-vindo ao Gerador de Nome de Monstro!")
try:
    quantidade = int(input("Quantos nomes de monstros você gostaria de gerar? "))
    if quantidade <= 0:
        print("Por favor, insira um número maior que zero!")
    else:
        print("\nAqui estão seus monstros:")
        for _ in range(quantidade):
            print("-", gerar_nome_monstro())
except ValueError:
    print("Por favor, insira um número válido!")