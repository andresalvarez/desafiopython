
import pytest

from  aleatorio import Aleatorio 

aleatorio = Aleatorio("Aleatorio")


def test_nao_pode_comprar_sem_saldo():
  
  aleatorio.saldo = 0

  pode_comprar = aleatorio.vai_comprar(100,50)

  assert not pode_comprar



