from flask_restplus import Api

from consulta.blueprints.resources.especialidade import EspecialidadeResource
from consulta.blueprints.resources.medico import MedicoResource
from consulta.blueprints.resources.agendamento import AgendamentoResource

BASE_PATH = '/api'


def init_app(app):
    api = Api(
        doc='/v1/api-docs',
        version='0.0.1',
        base_url=BASE_PATH,
        default_mediatype='application/json',
        catch_all_404s=True,
        path=BASE_PATH
    )

    api.add_resource(EspecialidadeResource, f'{BASE_PATH}/especialidades', methods=['GET'])
    api.add_resource(MedicoResource, f'{BASE_PATH}/medicos', methods=['POST'])
    api.add_resource(AgendamentoResource, f'{BASE_PATH}/agendamento', methods=['POST', 'GET'])

    api.init_app(app)
