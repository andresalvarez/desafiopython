class Jogador:
    """
        classe base para os jogadores
    """
    def __init__(self, nome):        
        self.saldo = 300
        self.posicao = 0
        self.nome = nome
        
    
    def vai_comprar(self, valor, aluguel):
        """
            Decide se jogador vai comprar propriedade, comportamento padrão nunca compra
        """
        return False

    def adiciona_saldo(self, saldo):
        """
            adiciona valor ao saldo do jogador
        """
        self.saldo += saldo

    def tem_saldo(self):
        """
            retorna  true se o jogador tem saldo
        """
        return self.saldo > 0



    