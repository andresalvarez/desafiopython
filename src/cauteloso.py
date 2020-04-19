from jogador import Jogador

class Cauteloso(Jogador):
    """
        Classe que sobrescreve o jogador para definir comportamento do jogador cauteloso
    """

    def __init__(self, nome):
        super().__init__(nome)

    def vai_comprar(self, valor, aluguel):  
        """
            O jogador cauteloso compra qualquer propriedade desde que ele 
            tenha uma reserva de 80 saldo sobrando
            depois de realizada a compra
        """    
        
        return ((self.saldo - valor) >= 80)