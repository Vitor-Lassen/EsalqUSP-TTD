from .entities import *
from .value_objects import *
from typing import Dict 
from datetime import date

class MatriculaService: 
    def __init__(self):
        self.matriculas = Dict[int, Matricula] = {}
        self.alinos: Dict[int, Aluno] = {}
        self.treinamentos: Dict[int, Treinamento] = {}
        self.proximo_id_matricula = 1

    def matricular_aluno(self, aluno:Aluno, treinamento: Treinamento, periodo: Periodo, data_inicio:date) -> Matricula:
        matricula = Matricula(
            id = self.proximo_id_matricula,
            aluno = aluno,
            treinamento = treinamento,
            periodo = periodo,
            data_matricula = date.today()
        )
        
        self.matriculas[matricula.id] = matricula
        self.proximo_id_matricula += 1
        return matricula