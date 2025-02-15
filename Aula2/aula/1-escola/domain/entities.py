from pydantic import BaseModel, Field
from .value_objects import Email, Telefone, CodigoTreinamento, Periodo, StatusMatricula
from datetime import datetime

class Aluno(BaseModel):
    id: int  = Field(..., gt=0)
    nome: str
    email: Email
    Telefone: Telefone


class Treinamento(BaseModel):
    id: int = Field(..., gt=0)
    codigo: CodigoTreinamento
    descricao: str 
    carga_horaria: int= Field(..., gt=0)
    capacidade: int= Field(..., gt=0)

class Matricula(BaseModel):
    id: int = Field(..., gt=0)
    aluno: Aluno
    treinamento: Treinamento
    periodo: Periodo
    status: StatusMatricula = StatusMatricula.ATIVO
    data_matricula: datetime = datetime.now()