from uuid import uuid4
from domain.task.task_entity import Task
import pytest

class TestTask:
    #TESTE PARA VERIFICAR O CONSTRUTOR DA CLASSE TAREFA
    def test_task_initialization(self):
        task_id = uuid4()
        user_id = uuid4()
        title = "Tarefa 1"
        description = "Descrição da tarefa 1"
        completed = False

        task = Task(id= task_id, 
                    user_id= user_id, 
                    title= title,
                    description= description, 
                    completed= completed)

        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    #TESTE PARA VALIDAÇÃO DO ID DA TAREFA
    def test_task_id_validation(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            task = Task(id="Invalido", 
                        user_id=uuid4(), 
                        title="Tarefa 1", 
                        description="Descrição da tarefa 1", 
                        completed=False)
            
    #TESTE PARA VALIDACAO DO ID USUARIO
    def test_task_user_id_validation(self):
        with pytest.raises(Exception, match="user_id must be an UUID"):
            task = Task(id=uuid4(), 
                        user_id="Invalido", 
                        title="Tarefa 1", 
                        description="Descrição da tarefa 1", 
                        completed=False)
    
    #TESTE PARA VALIDAÇÃO DO TITULO DA TAREFA
    def test_task_title_validation(self):
        with pytest.raises(Exception, match="title must be a string"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title="", 
                        description="Descrição da tarefa 1", 
                        completed=False)
        with pytest.raises(Exception, match="title must be a string"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title=123, 
                        description="Descrição da tarefa 1", 
                        completed=False)
    
    #TESTE PARA VALIDAÇÃO DA DESCRIÇÃO DA TAREFA
    def test_task_description_validation(self):
        with pytest.raises(Exception, match="description must be a string"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title="Tarefa 1", 
                        description="", 
                        completed=False)
        with pytest.raises(Exception, match="description must be a string"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title="Tarefa 1", 
                        description=123, 
                        completed=False)
    
    #TESTE PARA VALIDAÇÃO DO STATUS DA TAREFA
    def test_task_completed_validation(self):
        with pytest.raises(Exception, match="completed must be a boolean"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title="Tarefa 1", 
                        description="Descrição da tarefa 1", 
                        completed="")
        with pytest.raises(Exception, match="completed must be a boolean"):
            task = Task(id=uuid4(), 
                        user_id=uuid4(), 
                        title="Tarefa 1", 
                        description="Descrição da tarefa 1", 
                        completed="Invalido")
            
    #TESTE PARA VERIFICAR SE UMA TAREFA FOI CONCLUIDA COM UMA FUNÇÃO mark_as_completed
    def teste_mark_as_completed(self):
        task = Task(id=uuid4(), 
                    user_id=uuid4(), 
                    title="Tarefa 1", 
                    description="Descrição da tarefa 1", 
                    completed=False)
        
        task.mark_as_completed()
        assert task.completed == True