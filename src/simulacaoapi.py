
import numpy as np
import pandas as pd
from jogo import Jogo
from flask import Flask, jsonify, request, make_response, json
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import BadRequest





app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "v1"
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Desafio Python"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/simula', methods=['POST'])
def simular_jogo():
    """
        Endpoint para simular N partidas de um jogo
    """
    NroSimulacoes = request.json
    numerosimulacoes = int(NroSimulacoes["NroSimulacoes"])
    resultados =[]
    for partida in range (1,numerosimulacoes+1):
        jogo = Jogo()
        result = jogo.rodar_partida()
  
        resultados.append(result)
    
    saida =  {}
    saida["ResultadoPartidas"] = resultados

    df_result = pd.DataFrame.from_dict(resultados)
    timeout = df_result['Timeout'].sum()
    media_turnos = df_result['Turno'].mean()

    vencedores = df_result.groupby(['Vencedor']).agg({'Vencedor': 'count'})

    porcentagem_vitoria = vencedores.div(len(df_result), level='Vencedor') * 100
   
    #Quantas partidas terminam por time out (1000 rodadas);
    saida["NroPartidastimeout"] = timeout

    #Quantos turnos em média demora uma partida;
    saida["MediaTurnos"] = media_turnos

    
    #Qual a porcentagem de vitórias por comportamento dos jogadores;
    saida["PorcentagemVitorias"] = porcentagem_vitoria.to_dict()
    
    #Qual o comportamento que mais vence.    
    saida["MelhorComportamento"] = porcentagem_vitoria[porcentagem_vitoria["Vencedor"]==porcentagem_vitoria.max()[0]].index.values[0]
    
    return make_response(json.dumps(saida, cls=NpEncoder))

if __name__ == "__main__":
    app.run(debug=True)



class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)