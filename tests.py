from unittest import TestCase, main

from desafio import solucao, indices


class TestDesafio(TestCase):

    def test_todas_opcoes_estao_erradas(self):
        entrada = indices
        esperado = [1, 2, 3]
        self.assertEqual(solucao(entrada), (esperado[0] or esperado[1] or esperado[2]))

    def test_somente_a_arma_esta_correta(self):
        entrada = [indices[0], indices[1] + 1, indices[2]]
        esperado = [1, 3]
        self.assertEqual(solucao(entrada), (esperado[0] or esperado[1]))

    def test_somente_o_assassino_esta_correto(self):
        entrada = [indices[0] + 1, indices[1], indices[2]]
        esperado = 1
        self.assertEqual(solucao(entrada), esperado)

    def test_todas_opcoes_corretas(self):
        entrada = [indices[0] + 1, indices[1] + 1, indices[2] + 1]
        esperado = 0
        self.assertEqual(solucao(entrada), esperado)


main()
