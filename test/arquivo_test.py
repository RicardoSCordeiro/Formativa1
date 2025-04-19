"""
Este módulo contém testes unitários para as funções implementadas no módulo src.main.
Ele verifica o comportamento das funções gerar_nome_monstro, prefixos e sufixos.
"""

import unittest
from src.main import gerar_nome_monstro, prefixos, sufixos

class TestGeradorDeNomeMonstro(unittest.TestCase):

    def test_nome_valido(self):
        """Teste básico para garantir que o nome gerado é válido."""
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        self.assertTrue(len(nome_monstro) > 0)

    def test_prefixo_presente(self):
        """Verifica se o prefixo do nome gerado pertence à lista de prefixos."""
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        # Verifica se o nome começa com algum prefixo da lista
        prefixo = next((p for p in prefixos if nome_monstro.startswith(p)), None)
        self.assertIsNotNone(prefixo, f"Prefixo inválido em {nome_monstro}")

    def test_sufixo_presente(self):
        """Verifica se o sufixo do nome gerado pertence à lista de sufixos."""
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        # Verifica se o nome termina com algum sufixo da lista
        sufixo = next((s for s in sufixos if nome_monstro.endswith(s)), None)
        self.assertIsNotNone(sufixo, f"Sufixo inválido em {nome_monstro}")

    def test_listas_vazias(self):
        """Garante que o comportamento é correto quando as listas são vazias."""
        with self.assertRaises(ValueError):  # Exceção correta agora
            gerar_nome_monstro([], [])

    def test_retorno_tipo_string(self):
        """Certifica que o tipo do retorno da função é sempre uma string."""
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        self.assertIsInstance(nome_monstro, str)

if __name__ == "__main__":
    unittest.main()

