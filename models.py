# models.py

from app import db


class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'

    id_fornecedor = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18), nullable=False, index=True)
    razao_social = db.Column(db.String(200))
    nome = db.Column(db.String(150), nullable=False)

    def __init__(self, cnpj, razao_social, nome):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome = nome

    def __repr__(self):
        return '<Fornecedor %r>' % self.nome
