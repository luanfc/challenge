from unitest import TestCase, main
from desafio import solucao
"""
Ordem dos inputs: S, A, L

input: 1, 1, 1
output: 1, ou 2, ou 3 (todos estão incorreto)

input: 3, 1, 3
output: 1, ou 3 (somente o local está correto)

input: 5, 3, 4
output: 1 (somente o assassino está incorreto)

input: 2, 3, 4
output: 0 (todos corretos)
"""

class TestCifraCesar(TestCase):
	def test_solucao_entrada_111_retorna_1_ou_2_ou_3(self)
		entrada = [1, 1, 1]
		esperado = [1, 2, 3]
		self.assertEqual(solucao(entrada), esperado)
	def test_solucao_entrada_313_retorna_1_ou_3(self)
		pass
	def test_solucao_entrada_534_retorna_1(self)
		pass
	def test_solucao_entrada_234_retorna_0(self)
		pass

main()
