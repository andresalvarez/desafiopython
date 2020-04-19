import pytest
from exigente import Exigente
from propriedade import Propriedade



  
exigente = Exigente("exigente")


def test_pode_comprar_quando_houver_saldo_e_aluguel_maior_50():
  
  exigente.saldo = 200
  deveComprar = exigente.vai_comprar(100,50)

  assert (deveComprar)

def test_pode_comprar_quando_houver_saldo_e_aluguel_maior_50():
  
  exigente.saldo = 200
  deveComprar = exigente.vai_comprar(100,40)

  assert not (deveComprar)

def test_nao_pode_comprar_sem_saldo():

  exigente.saldo = 0

  deveComprar = exigente.vai_comprar(100,60)

  assert not (deveComprar)



def test_nao_pode_comprar_com_saldo_final_menor_que_80():
  exigente.saldo = 100
 

  deveComprar = exigente.vai_comprar(30,30)

  assert not (deveComprar)
