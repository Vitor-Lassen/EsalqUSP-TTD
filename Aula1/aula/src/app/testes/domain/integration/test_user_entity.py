from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4

class TesteUserWithTasks:

    #TESTE PARA ADICIONAR TAREFA AO USUÁRIO
    def test_collect_tasks(self):
        user = User(id=uuid4(), name="Willian")
        task1 = Task(id=uuid4(), user_id=user.id, title="Tarefa 1", description="Descrição da tarefa 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Tarefa 2", description="Descrição da tarefa 2", completed=False)
        user.collect_tasks([task1, task2])
        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks

    # TESTE PARA CONTABILIZAR TAREFAS PENDENTES DE UM USUÁRIO
    def test_count_pending_tasks(self):
        user = User(id=uuid4(), name="Willian")
        task1 = Task(id=uuid4(), user_id=user.id, title="Tarefa 1", description="Descrição da tarefa 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Estudar Testes unitatios ", description="Descrição da tarefa 2", completed=False)
        task3 = Task(id=uuid4(), user_id=user.id, title="Tarefa 3", description="Descrição da tarefa 3", completed=False)
        
        user.collect_tasks([task1, task2, task3])
        task1.mark_as_completed()
        pending_count = user.count_pending_tasks()
        assert pending_count == 2

    # TESTE A QUANTIDADE DE TAREFAS PENDENTES DE UM USUÁRIO É CRIADO
    def teste_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name="Willian")
        pending_count = user.count_pending_tasks()
        assert pending_count == 0

    #TESTAR QUANDO TODAS AS TAREFAS DO USUÁRIO ESTÃO COMPLETADAS
    def test_all_task_complited(self):
        user = User(id=uuid4(), name="Willian")
        task1 = Task(id=uuid4(), user_id=user.id, title="Tarefa 1", description="Descrição da tarefa 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Tarefa 2", description="Descrição da tarefa 2", completed=False)
        task3 = Task(id=uuid4(), user_id=user.id, title="Tarefa 3", description="Descrição da tarefa 3", completed=False)
        
        user.collect_tasks([task1, task2, task3])
        #Usuario com todas tarefas pendentes 
        
        user.tasks[0].mark_as_completed()
        user.tasks[1].mark_as_completed()
        user.tasks[2].mark_as_completed()
        #usuario com todas tarefas completadas

        pending_count = user.count_pending_tasks()
        assert pending_count == 0