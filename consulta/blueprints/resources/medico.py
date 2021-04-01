import json

from flask import jsonify, request
from flask_restplus import Resource

from consulta.blueprints.services.medico import MedicoService


class MedicoResource(Resource):
    def post(self):
        medico = MedicoService()
        dados = json.loads(request.data)

        retorno = medico.listar_por_especialidade(dados)
        return jsonify(retorno)
