from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_maior_e_menor_valor_lance_adicionados_ordem_crescente(self):
        mc_gorila = Usuario('MC Gorila')
        yuri = Usuario('Yuri')

        lance_do_mc_gorila = Lance(mc_gorila, 200.0)

        lance_do_yuri = Lance(yuri, 250.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_mc_gorila)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 200
        maior_valor_esperado = 250

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_maior_menor_valor_adicionados_descrecenente(self):
        mc_gorila = Usuario('MC Gorila')
        yuri = Usuario('Yuri')

        lance_do_mc_gorila = Lance(mc_gorila, 200.0)

        lance_do_yuri = Lance(yuri, 250.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_mc_gorila)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 200
        maior_valor_esperado = 250

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

