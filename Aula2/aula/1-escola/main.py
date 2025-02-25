from domain.entities import Aluno, Treinamento, Matricula
from domain.value_objects import * 

"""
Criar instancias de alunos
"""

aluno1 = Aluno(id=1, nome="João", email=Email(email="joão@email.com"), telefone=Telefone(numero="11-99999-9999"))
aluno2 = Aluno(id=2, nome="Maria", email=Email(email="maria@email.com"), telefone=Telefone(numero="11-99999-8888"))
aluno3 = Aluno(id=3, nome="José", email=Email(email="jose@email.com"), telefone=Telefone(numero="11-7777-7777"))

print("Alunos Criados")

""""
Criar instancias de treinamentos"""

treinamento1 = Treinamento(id=1, codigo=CodigoTreinamento(codigo="IA01"), descricao="Curso de funcamentos de IA", carga_horaria=40, capacidade=20)
treinamento2 = Treinamento(id=2, codigo=CodigoTreinamento(codigo="IA02"), descricao="Curso de IA aplicada", carga_horaria=40, capacidade=2)
treinamento3 = Treinamento(id=3, codigo=CodigoTreinamento(codigo="PY05"), descricao="pythom avançado", carga_horaria=120, capacidade=20)

print("Treinamentos Criados")         