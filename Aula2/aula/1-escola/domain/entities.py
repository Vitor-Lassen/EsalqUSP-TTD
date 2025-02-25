from pydantic import BaseModel, Field
from .value_objects import Email, Telefone, CodigoTreinamento, Periodo, StatusMatricula
from datetime import date

class Aluno(BaseModel):
    """args: id, nome, email, telefone"""
    id: int  = Field(..., gt=0)
    nome: str
    email: Email
    telefone: Telefone


class Treinamento(BaseModel):
    """Args: Id, Código, Descrição, Carga Horária, Capacidade"""
    id: int = Field(..., gt=0)
    codigo: CodigoTreinamento
    descricao: str 
    carga_horaria: int= Field(..., gt=0)
    capacidade: int= Field(..., gt=0)

class Matricula(BaseModel):
    """Args: Id, Alunos, Treinamentos, Período, Status, Data de Matrícula"""
    id: int = Field(..., gt=0)
    aluno: Aluno
    treinamento: Treinamento
    periodo: Periodo
    status: StatusMatricula = StatusMatricula.ATIVO
    data_matricula: date 