import random
from impulsivo import Impulsivo
from aleatorio import Aleatorio
from exigente import Exigente
from cauteloso import Cauteloso
from propriedade import Propriedade

class Jogo:

    def __init__(self):
        self.vencedor = None
        self.turnos = 0
        self.propriedades = [
            Propriedade('Inicio', 0, 0),
            Propriedade('Botafogo', 110, 35),
            Propriedade('Flamengo', 120, 30),
            Propriedade('Interlagos', 80, 20),
            Propriedade('Morumbi', 90, 25),
            Propriedade('Leblon', 200, 70),
            Propriedade('Nossa Senhora Copacabana', 120, 40),
            Propriedade('Faria Lima', 150, 50),
            Propriedade('Nove de julho', 70, 10),
            Propriedade('Rebouças', 90, 20),
            Propriedade('Jardim Paulista', 110, 35),
            Propriedade('Av  Paulista', 130, 45),
            Propriedade('Av Brasil', 120, 40),
            Propriedade('Jardim Europa', 100, 30),
            Propriedade('Santo Amaro', 50, 5),
            Propriedade('Vieira Souto', 220, 80),
            Propriedade('Av Atlantica', 110, 35),
            Propriedade('Ipanema', 120, 40),
            Propriedade('Copacabana', 130, 45),
            Propriedade('Tatuape', 60, 10),
            Propriedade('Berrini', 70, 15)
        ]
        self.jogadores = {
           "Impulsivo" : Impulsivo('Impulsivo'),
           "Aleatorio" : Aleatorio('Aleatorio'),
           "Exigente" :  Exigente('Exigente'),
           "Cauteloso" :  Cauteloso('Cauteloso')
        }

    def rodar_partida(self):
        Lider = None
        

        for rodada in range(1, 1001):
            turnos = rodada
            for key, jogador in self.jogadores.items():
                if jogador.tem_saldo():
                    movimentos = self.jogar_dado()
                    novaposicao, volta = self.pular_posicao(jogador.posicao, movimentos)
                    jogador.posicao = novaposicao
                    ### caso o jogador de uma volta completa ele rece 100 de saldo
                    if volta:
                        jogador.adiciona_saldo(100)

                    #obtem a propriedade que o jogador parou
                    propriedade = self.propriedades[jogador.posicao]

                    self.trata_aluguel(propriedade, jogador)                    
                    
                    self.comprar_propriedade(propriedade, jogador)
                    
                    self.tratar_falencia(jogador)
            
            lider_atual , finaliza_partida = self.obter_lideranca()
            
            if finaliza_partida or turnos == 1000:
                Lider = lider_atual.nome
                break

        resultado = {
            "Vencedor" :Lider,
            "Timeout" : (turnos == 1000),
            "Turno"  : turnos

        }
         
        return resultado
        
        


    def tratar_falencia(self, jogador): 
        """
            Retirar todas as propriedades do jogador e coloca-las disponiveis
        """   
        if not jogador.tem_saldo():         
            propriedades= [ x for x in self.propriedades if x.pertence(jogador.nome) ]
            for propriedade in propriedades:
                propriedade.proprietario = None

    def trata_aluguel(self, propriedade, jogador):
        """
            Verifica se a propriedade está vendida e caso o jogador nao a possua cobra o aluguel
        """
        if propriedade.vendida() and not propriedade.pertence(jogador.nome): 
            jogador.saldo -= propriedade.valorDoAluguel
            self.jogadores[propriedade.proprietario.nome].saldo += propriedade.valorDoAluguel

    def comprar_propriedade(self, propriedade, jogador):
        """
            Verifica se a propriedade tem dono e caso negativo efetua
            a compra pelo jogador

        """
        if not propriedade.vendida(): 
            if jogador.vai_comprar(propriedade.valorDaVenda , propriedade.valorDoAluguel):    
                jogador.saldo -= propriedade.valorDaVenda
                propriedade.proprietario = jogador

    def jogar_dado(self):
        """
            Retorna um valor aletório de 1 a 6
        """
        return random.randint(1, 6)

        
    def pular_posicao(self, posicaoinicial,quantidademovimentos):
         """
            retorna a posicao de acordo com o movimento dos dados
            segundo retorno retorna true caso de uma volta completa
         """
         posicao_futura = (posicaoinicial + quantidademovimentos) % len(self.propriedades)
         return posicao_futura, posicao_futura < posicaoinicial

    
    def obter_lideranca(self):
        """
            Obtem jogador que finalizou o jogo com maior saldo,
            caso somente tenha um jogador que nao tenha falido sinaliza para finalizar o jogo 
        """
        jogadores = self.jogadores.values() 
        jogadores_partida = sum(j.tem_saldo() for j in jogadores)
        lider = max(jogadores, key=lambda jogador: jogador.saldo)
        finaliza_partida = jogadores_partida < 2
        return lider, finaliza_partida
            