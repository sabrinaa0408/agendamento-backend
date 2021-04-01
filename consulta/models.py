from consulta.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Medico(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade_id = db.Column(db.Integer, db.ForeignKey("especialidade.id"), nullable=False)
    serialize_rules = ('-related-models.especialidade',)

    especialidade = db.relationship("Especialidade", backref="especialidade")

    @staticmethod
    def to_dict_medico(medico_id=0):
        if medico_id:
            medico = Medico.query.filter(Medico.id==medico_id).first()
            especialidade = Especialidade.to_dict_espec(espec_id=medico.especialidade_id)
            return {
                "nome": medico.nome,
                "especialidade": especialidade
            }


class Agendamento(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey("medico.id"), nullable=False)

    medico = db.relationship("Medico", backref="medico")

    def to_dict(self):
        if self.medico_id:
            medicos = Medico.to_dict_medico(medico_id=self.medico_id)
        return {
            "data": self.data,
            "id": self.id,
            "medicos": medicos
        }


class Especialidade(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    @staticmethod
    def to_dict_espec(espec_id=0):
        if espec_id:
            especialidade = Especialidade.query.filter(Especialidade.id==espec_id).first()
            return especialidade.nome
