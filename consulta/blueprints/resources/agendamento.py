import json

from flask import jsonify, request
from flask_restplus import Resource

from consulta.blueprints.services.agendamento import AgendamentoService


class AgendamentoResource(Resource):
    def post(self):
        agendamento = AgendamentoService()
        dados = json.loads(request.data)

        retorno = agendamento.agendar_consulta(dados)
        return jsonify(retorno)
    
    def get(self):
        agendamento = AgendamentoService()

        retorno = agendamento.listar_agendamentos()
        return jsonify(retorno)
