import random
import os

quantidade = int(os.getenv("QUANTIDADE", 10))

prefixos = ["Giga", "Mega", "Mini", "Dark", "Fire", "Ice", "Thunder"]
sufixos = ["zilla", "tron", "monster", "creep", "fang", "storm", "wolf"]

def gerar_nome_monstro(prefixos, sufixos):
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    return prefixo + sufixo

print("Bem-vindo ao Gerador de Nome de Monstro!")
print(f"Gerando {quantidade} nomes de monstros!\n")
print("Aqui estão seus monstros:")
for _ in range(quantidade):
    print("-", gerar_nome_monstro(prefixos, sufixos))


