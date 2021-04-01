from consulta.models import Especialidade


class EspecialidadeService:
    @staticmethod
    def listar():
        especialidades = Especialidade.query.all()
        return {"especialidades": [especialidade.to_dict(rules=('-especialidade', '-especialidade')) for especialidade in especialidades]}
