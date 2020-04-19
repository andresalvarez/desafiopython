
import pytest

from  impulsivo import Impulsivo 

impulsivo = Impulsivo("impulsivo")


def test_nao_pode_comprar_sem_saldo():
  
  impulsivo.saldo = 0

  pode_comprar = impulsivo.vai_comprar(100,50)

  assert not pode_comprar

def test_pode_comprar_se_tiver_saldo():
  
  impulsivo.saldo = 100

  pode_comprar = impulsivo.vai_comprar(100,50)

  assert pode_comprar

