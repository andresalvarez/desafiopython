import pytest

from  propriedade import Propriedade 
from impulsivo import Impulsivo

nome = "Teste"
valorDaVenda = 250
valorDoAluguel = 25
propriedade = Propriedade(nome, valorDaVenda, valorDoAluguel)

def test_criar_propriedade():
    teste = {
        'nome': nome,
        'valorDaVenda': valorDaVenda,
        'valorDoAluguel': valorDoAluguel,
        'proprietario': None
    }

    assert (teste == propriedade.__dict__)

def test_setar_proprietario():
    propriedade.proprietario = Impulsivo("Impulsivo")

    assert (propriedade.proprietario!=None)



def test_se_nao_pertence_jogador():

    propriedade.proprietario = Impulsivo("Impulsivo")


    assert not (propriedade.pertence("Cauteloso"))

def test_propriedade_pertence_jogador():
    
    propriedade.proprietario = Impulsivo("Impulsivo")


    assert (propriedade.pertence("Impulsivo"))