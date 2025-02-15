from uuid import uuid4
from domain.user.user_entity import User
import pytest

class TesteUser: 
    #TESTE PARA CONSTRUIR O USUÁRIO
    def teste_user_initialization(self):
        user_id = uuid4()
        user_name = "Alexandre"
        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name

    #TESTE PARA VALIDAÇÃO DO ID DO USUARIO 
    def teste_user_id_validation(self):

        with pytest.raises(Exception, match="id must be an UUID"):
            user = User(id="Invalido", name="Gabriel")

    #TESTE PARA VALIDAÇÃO DO NOME DO USUARIO
    def teste_user_name_validation(self):
        with pytest.raises(Exception, match="name is required"):
            user = User(id=uuid4(), name="")
        with pytest.raises(Exception, match="name is required"):
            user = User(id=uuid4(), name=123)
        
    