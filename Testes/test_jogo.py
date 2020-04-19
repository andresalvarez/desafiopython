import unittest
from jogo import Jogo
from impulsivo import Impulsivo
from cauteloso import Cauteloso



                     
                    
                    
                    
 #                  
 #   

def test_trataraluguel_pagar():
    jogo = Jogo()
    jogadorPagador = jogo.jogadores["Impulsivo"]
    saldoinicial = jogadorPagador.saldo
    jogadorRecebedor =   jogo.jogadores["Cauteloso"]
    jogo.propriedades[2].proprietario = jogadorRecebedor

    aluguel = jogo.propriedades[2].valorDoAluguel
    jogo.trata_aluguel(jogo.propriedades[2], jogadorPagador)    

    assert  jogadorPagador.saldo == saldoinicial - aluguel
    
def test_trataraluguel_receber():
    jogo = Jogo()
    jogadorPagador = jogo.jogadores["Impulsivo"]
    
    jogadorRecebedor =   jogo.jogadores["Cauteloso"]
    saldoinicial = jogadorRecebedor.saldo
    jogo.propriedades[2].proprietario = jogadorRecebedor

    aluguel = jogo.propriedades[2].valorDoAluguel
    jogo.trata_aluguel(jogo.propriedades[2], jogadorPagador)    

    assert  jogadorRecebedor.saldo == (saldoinicial + aluguel)


def test_comprar_propriedade():
    jogo = Jogo()
    jogadorPagador = jogo.jogadores["Impulsivo"]
    saldoinicial = jogadorPagador.saldo
    print(saldoinicial)
    valorpropriedade = jogo.propriedades[2].valorDaVenda
    
    jogo.comprar_propriedade(jogo.propriedades[2], jogadorPagador)    

    print(jogadorPagador.saldo)
    print(saldoinicial - valorpropriedade)
    assert jogadorPagador.saldo == (saldoinicial - valorpropriedade)

def test_Retirar_jogador_do_jogo():     
    jogo = Jogo()
    jogadorPagador = jogo.jogadores["Impulsivo"]
    jogadorPagador.saldo = 1000
    
    
    
    jogo.comprar_propriedade(jogo.propriedades[2], jogadorPagador)  
    jogo.comprar_propriedade(jogo.propriedades[3], jogadorPagador)    
    jogo.comprar_propriedade(jogo.propriedades[7], jogadorPagador)      

    jogadorPagador.saldo = -100

    propriedadevendidas = len( [p for p in jogo.propriedades if p.proprietario != None])
    assert propriedadevendidas == 3
    jogo.tratar_falencia(jogadorPagador)

    propriedadevendidas = len( [p for p in jogo.propriedades if p.proprietario != None])
    assert propriedadevendidas == 0
      


def test_Continuar_Jogo():
    jogo = Jogo()
    jogo.turnos = 50
    lider_atual , finaliza_partida = jogo.obter_lideranca()

    assert not finaliza_partida

def test_ObterVencedor():
    jogo = Jogo()
    jogadorganhador = jogo.jogadores["Impulsivo"]
    jogadorganhador.saldo = 1000
    lider_atual , finaliza_partida = jogo.obter_lideranca()

    assert lider_atual == jogadorganhador

def test_finaliza_partida_por_falencia ():
    jogo = Jogo()
    jogo.jogadores["Impulsivo"].saldo = -1
    
    jogo.jogadores["Exigente"].saldo = -1
    
    jogo.jogadores["Cauteloso"].saldo = -1

 
    lider_atual , finaliza_partida = jogo.obter_lideranca()

    assert finaliza_partida

