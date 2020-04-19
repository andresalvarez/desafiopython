import pytest
from cauteloso import Cauteloso
from propriedade import Propriedade



  
cauteloso = Cauteloso("Cauteloso")


def test_pode_comprar_quando_houver_saldo_e_sobrar_mais_80():
  cauteloso.saldo = 200
  deveComprar = cauteloso.vai_comprar(100,50)

  assert (deveComprar)

def test_nao_pode_comprar_sem_saldo():

  cauteloso.saldo = 0

  deveComprar = cauteloso.vai_comprar(100,50)

  assert not (deveComprar)



def test_nao_pode_comprar_com_saldo_final_menor_que_80():
  cauteloso.saldo = 100
 

  deveComprar = cauteloso.vai_comprar(30,30)

  assert not (deveComprar)
