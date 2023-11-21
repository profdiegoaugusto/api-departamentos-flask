from sqlalchemy import Column, BigInteger, String, Text

from app.database import Base


class Departamento(Base):

    __tablename__ = 'Departamento'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(75))
    descricao = Column(Text, nullable=True)

    def __init__(self, nome=None, descricao=None):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return f'<Departamento {self.nome!r}>'
