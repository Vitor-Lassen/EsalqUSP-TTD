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
