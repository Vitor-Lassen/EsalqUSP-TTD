from infra.user.in_memory_use_repositoy import InMemoryRepository
from domain.user.user_repository_interface import UserRepositoryInterface
from applicantion.user.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from uuid import UUID

class TestCreateUser: 
    #TESTE PARA CRIAR UM USUARIO COM DADOS VÁLIDOS
    def test_create_user_with_valid_data(self):
        repository = InMemoryRepository()

        use_case = CreateUserUseCase(repository=repository)
        request = CreateUserRequest(name="Willian")

        response = use_case.execute(request)

        assert len(repository.users) == 1
        assert isinstance(response.id, UUID)

        persit_user = repository.users[0]
        
        assert persit_user.id == response.id
        assert persit_user.name == "Willian"