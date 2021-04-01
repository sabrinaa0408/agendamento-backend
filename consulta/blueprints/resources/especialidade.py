from flask import jsonify
from flask_restplus import Resource

from consulta.blueprints.services.especialidade import EspecialidadeService


class EspecialidadeResource(Resource):
    def get(self):
        especialidade = EspecialidadeService()

        retorno = especialidade.listar()
        return jsonify(retorno)
