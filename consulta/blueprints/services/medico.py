from consulta.models import Medico


class MedicoService:
    @staticmethod
    def listar_por_especialidade(dados):
        medicos = Medico.query.filter(Medico.especialidade_id==dados[0]).all()
        return {"medicos": [medico.to_dict(rules=('-medico', '-medico', '-especialidade_id', '-especialidade')) for medico in medicos]}
