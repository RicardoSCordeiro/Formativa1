import unittest
from src.main import gerar_nome_monstro, prefixos, sufixos

class TestGeradorDeNomeMonstro(unittest.TestCase):

    def test_nome_valido(self):
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        self.assertTrue(len(nome_monstro) > 0)

    def test_prefixo_presente(self):
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        prefixo = nome_monstro.split(sufixos[0])[0]
        self.assertIn(prefixo, prefixos)

    def test_sufixo_presente(self):
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        sufixo = nome_monstro.split(prefixos[0])[-1]
        self.assertIn(sufixo, sufixos)

    def test_listas_vazias(self):
        with self.assertRaises(IndexError):
            gerar_nome_monstro([], [])

    def test_retorno_tipo_string(self):
        nome_monstro = gerar_nome_monstro(prefixos, sufixos)
        self.assertIsInstance(nome_monstro, str)

if __name__ == "__main__":
    unittest.main()
