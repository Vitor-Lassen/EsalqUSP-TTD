from domain.user.user_entity import User
from infra.user.in_memory_use_repositoy import  InMemoryRepository
from uuid import uuid4

class TestSaveUser:
    #TESTAR SE É POSSÍVEL SALVAR USUARIOS NO REPOSITÓRIO
    def test_can_save_user(self):
        repository = InMemoryRepository()
        user1 = User (id=uuid4(), name='user1')
        user2 = User (uuid4(), 'user2')

        repository.save(user1)
        repository.save(user2)

        # VERIFICAR SE OS USUARIOS ESTÃO NO REPOSITÓRIO E SE A LISTA TEM 2 USUARIOS\

        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2

class TestGetUserById:
    #TESTAR SE POSSIVEL RETORNAR UM USUARIO PELO ID
    def test_can_get_user_by_id(self):
        repository = InMemoryRepository()
        user1 = User (uuid4(), 'user1')
        user2 = User (uuid4(), 'user2')

        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user2.id)

        #VERIFICAR SE O USUARIO RETORNADO É O USUARIO 1
        assert user == user2

    #TESTAR SE O METODO RETORNA NONE QUANDO O USUARIO NÃO EXISTE

    def test_when_user_does_not_exit_should_return_none(self):
        repository = InMemoryRepository()
        user1 = User (uuid4(), 'user1')
        user2 = User (uuid4(), 'user2')

        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(uuid4())

        assert user == None

class TestUpdateUser: 
    #TESTAR SE É POSSIVEL ATUALIZAR O NOME DE UM USUARIO
    def test_can_update_user(self):
        repository = InMemoryRepository()
        user = User (id= uuid4(), name= 'user1')
        user2 = User (uuid4(), 'user2')
        repository.save(user)
        repository.save(user2)

        user.name = 'user_updated'
        
        repository.update(user)

        updated_user = repository.get_by_id(user.id)

        assert updated_user.name == 'user_updated'