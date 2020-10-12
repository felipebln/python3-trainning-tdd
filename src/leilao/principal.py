from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

mc_gorila = Usuario('MC Gorila')
yuri = Usuario('Yuri')

lance_do_mc_gorila = Lance(mc_gorila, 200.0)

lance_do_yuri = Lance(yuri, 250.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_mc_gorila)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} fez o lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)


print(f'O menor lance foi de {avaliador.menor_lance}')
print(f'O maior lance foi de {avaliador.maior_lance}')
