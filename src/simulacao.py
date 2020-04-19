
import numpy as np
import pandas as pd
from jogo import Jogo

if __name__ == "__main__": 
    """
        Iniciar a simulação de 300 partidas,
        imprimir o resultado de todas as partidas.
        Ao final imprimir as seguintes informações no console
            Quantas partidas terminam por time out (1000 rodadas);
            Quantos turnos em média demora uma partida;
            Qual a porcentagem de vitórias por comportamento dos jogadores;
            Qual o comportamento que mais vence.
    """

    numero_simulacoes = 300

    

    resultados =[]
    for partida in range (1,301):
        jogo = Jogo()
        result = jogo.rodar_partida()
        print(" Partida {rodada} - Vencedor : {vencedor} - Turno : {turno} - Timeout:{timeout}"
                .format(rodada=partida,vencedor=result['Vencedor'],turno=result['Turno'],timeout=result['Timeout'])
             )  
        resultados.append(result)
    
    
    df_result = pd.DataFrame.from_dict(resultados)
    timeout = df_result['Timeout'].sum()
    media_turnos = df_result['Turno'].mean()

    vencedores = df_result.groupby(['Vencedor']).agg({'Vencedor': 'count'})

    porcentagem_vitoria = vencedores.div(len(df_result), level='Vencedor') * 100
   
    #Quantas partidas terminam por time out (1000 rodadas);
    print("Partidas terminadas por timeout: {}".format(timeout))

    #Quantos turnos em média demora uma partida;
    print("Media de turnos por partida: {}".format(media_turnos))
    
    #Qual a porcentagem de vitórias por comportamento dos jogadores;
    print("Porcentagem de vitoria por comportamento")
    print(porcentagem_vitoria)
    
    #Qual o comportamento que mais vence.    
    print("Comportamento com mais vitorias:".format())
    print(porcentagem_vitoria[porcentagem_vitoria["Vencedor"]==porcentagem_vitoria.max()[0]])